project pkg {
    rpm {
        spec = "cuda-nvml.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
