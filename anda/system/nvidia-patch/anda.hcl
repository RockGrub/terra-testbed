project "pkg" {
    rpm {
        spec = "nvidia-patch.spec"
    }
   	labels {
		nightly = "1"
                subrepo = "nvidia"
	}
}
