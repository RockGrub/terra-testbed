project pkg {
    rpm {
        spec = "ruffle-nightly.spec"
        extra_repos = ["file:///__w/terra-testbed/terra-testbed/rpms"]
    }
}
