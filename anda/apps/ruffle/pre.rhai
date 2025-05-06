sh(`export ARCH=$(arch); mkdir -p rpms; pushd rpms; wget https://kojipkgs.fedoraproject.org//packages/curl/8.13.0/1.fc43/$ARCH/{curl,libcurl}-8.13.0-1.fc43.$ARCH.rpm; createrepo_c .; popd`, #{});
