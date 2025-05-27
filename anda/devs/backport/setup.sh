#!/usr/bin/bash

## Some sources need to be fetched BEFORE the build process
# This is because they are used to mass update the spec
# This is done ahead of time to update the spec dynamically for pulled versions
# This is near impossible to do in a normal update script due to the massive dependency cascade NodeJS packages have
# Doing it here also makes sure stuff only gets downloaded once
# Also I'm just better at scripting in Bash and calling the Rhai sh function hundreds of times times sounded like hell
# Have I mentioned I hate runtime languages?

# Enable logs for debugging
set -x
# I guess just $PWD doesn't work for this
builddir=$(echo $PWD)/anda/devs/backport

# We only need the tests folder so sourcing the whole repo is overkill, Git can make a tarball of specific directories

pushd $builddir
ver=$(cat ./*.spec | grep -P -m1 'Version:' | sed -e 's/Version://g' -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
url=$(sed -n 's/^URL:\s\(.*\)$/\1/p' ./*.spec | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
dir=$(basename $url | sed -s 's/\.git$//')

git clone --recurse-submodules -j$(nproc) $url.git

pushd $dir
# I'm not sure why .tar.bz2 is the tar format of choice for this but it's also what Fedora does so it's what I'm doing
git archive --format=tar --prefix=tests/ v${ver}:src/test/ | bzip2 > ../tests-${ver}.tar.bz2
popd
rm -rf $dir

## Fetch Node sources
export NVM_DIR=$builddir/.nvm
mkdir -p $NVM_DIR
## Disable debugging output for some of these because they spam
# Fedora is weeping
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash &>/dev/null
set +x
. "$NVM_DIR/nvm.sh"
. "$NVM_DIR/bash_completion"
# Use the latest Node for securty fixes, if possible
nvm install 24
set -x
npm install -g ${dir}@${ver} &>/dev/null
rm -rf .nvm/versions/node/v*/lib/node_modules/corepack
mv .nvm/versions/node/v*/lib/node_modules -t $builddir
## Make a tarball with the top dir the name of the package for %autosetup
# I don't get it but something about rpmuncompress removed the topdir of the tarball so I had to give it extra depth
# The package*.json files here that NPM put in the topdir are needed for the NodeJS macros to work
tar -czf $dir-$ver.tar.gz -C ../ $dir/node_modules

## Update the spec
# For loops are my best friend here
# These are done via global macros because they are unique
# I tried to match via \d. or \w. for versions and descriptions but perl regex kinda sucks, but grep's other regex modes weren't as helpful for this
set +x
for node in $(ls node_modules/$dir/node_modules | sed '/^\@.*/d;/^\.bin/d;/.*\.json/d'); do
  node_underscore=$(echo $node | sed 's/-/_/g;s/\./_/g')
  new_ver=$(cat node_modules/$dir/node_modules/${node}/package.json | grep -P -m1 '"version".*: ".*"' | sed 's/.*"version".*: "//g;s/",//g;s/-/~/g')
  new_desc=$(cat node_modules/$dir/node_modules/${node}/package.json | grep -P -m1 '"description".*: ".*"' | sed 's/.*"description".*: "//g;s/",//g;s/\&/\\\&/')
  sed -i "s|^%global ${node_underscore}_ver.*|%global ${node_underscore}_ver ${new_ver}|" ./*.spec
  if [[ $new_desc ]]; then
    sed -i "s|^%global ${node_underscore}_desc.*|%global ${node_underscore}_desc ${new_desc}|" ./*.spec
   else
    sed -i "s|^%global ${node_underscore}_desc.*|%global ${node_underscore}_desc The NodeJS ${node} package|" ./*.spec
  fi
done

for atnode in $(ls node_modules/$dir/node_modules | grep '@'); do
   atless=$(echo $atnode | sed 's/@//g')
    for subnode in $(ls node_modules/$dir/node_modules/$atnode); do
      subnode_underscore=$(echo $subnode | sed 's/-/_/g;s/\./_/g')
      new_ver=$(cat node_modules/$dir/node_modules/${atnode}/${subnode}/package.json | grep -P -m1 '"version".*: ".*"' | sed 's/.*"version".*: "//g;s/",//g;s/-/~/g')
      new_desc=$(cat node_modules/$dir/node_modules/${atnode}/${subnode}/package.json | grep -P -m1 '"description".*: ".*"'  | sed 's/.*"description".*: "//g;s/",//g;s/\&/\\\&/')
      sed -i "s|^%global ${atless}_${subnode_underscore}_ver.*|%global ${atless}_${subnode_underscore}_ver ${new_ver}|" ./*.spec
      if [[ $new_desc ]]; then
         sed -i "s|^%global ${atless}_${subnode_underscore}_desc.*|%global ${atless}_${subnode_underscore}_desc ${new_desc}|" ./*.spec
        else
         sed -i "s|^%global ${atless}_${subnode_underscore}_desc.*|%global ${atless}_${subnode_underscore}_desc The NodeJS ${atnode}-${subnode} package|" ./*.spec
      fi
     done
done

set -x
# Cleanup
rm -rf .nvm
rm -rf node_modules
rm -rfv *.json
rm -rf $HOME/.npm*
# Nuke Windows lines in the CI
#tr -d '\r' < ./*.spec > new.spec
#mv -f new.spec nodejs-backport.spec
popd
exit 0
