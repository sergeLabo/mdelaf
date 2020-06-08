#!/usr/bin/env python3.7


import os
from pathlib import Path
from textgenrnn import textgenrnn


def generate(textgen):
    """
    n=1,
    return_as_list=False,
    prefix=None,
    temperature=[1.0, 0.5, 0.2, 0.2],
    max_gen_length=300,
    interactive=False,
    top_n=3,
    progress=True
    """


    resp_list = textgen.generate(   n=1,
                                    return_as_list=False,
                                    temperature=0.5,
                                    return_as_list=True,
                                    prefix=None,
                                    max_gen_length=400,
                                    interactive=False,
                                    top_n=3
                                )

    resp = ""
    for item in resp_list:
        if item:
            resp += item + "\n"
    return resp


if __name__ == "__main__":
    textgen = textgenrnn('textgenrnn_weights.hdf5')
    generate(textgen)
