project pkg {
    rpm {
        spec = "ruffle-nightly.spec"
        extra_repos = ["file://./anda-build/rpm/rpms"]
    }
}
