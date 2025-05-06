project pkg {
        extra_repos = ["file://anda-build/rpm/rpms"]
    rpm {
        spec = "ruffle-nightly.spec"
    }
}
