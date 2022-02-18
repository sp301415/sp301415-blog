---
title: 애플 실리콘용 sage와 pwntools 설치 에러 해결
tags: ["개발", "암호학"]
description: 애플 실리콘에서 sage와 pwntools를 같이 설치할때 생기는 에러를 해결하는 법을 공유합니다.
---

### TL;DR

```
pip install unicorn
pip install pwntools
conda install sage
```
순으로 하면 된다.

CTF에서 crypto 문제를 풀 때, 수학 계산을 위해선 보통 `sage`를 쓰고, 소켓 통신을 위해선 `pwntools`를 쓴다. 나 같은 경우에는 conda 환경을 만들어서 사용하는데, 애플 실리콘이 들어간 맥을 사용하고부터는 두 개를 함께 설치하려고 하니 문제가 생겼다.

일단 conda를 이용해 `sage`를 설치하고, `pwntools`를 설치하려고 했더니 에러를 뿜는 것을 볼 수 있었다.
```
➜ conda install pwntools
Found conflicts! Looking for incompatible packages.
This can take several minutes.  Press CTRL-C to abort.
failed

UnsatisfiableError: The following specifications were found to be incompatible with each other:

Output in format: Requested package -> Available versions

```
`pip`을 이용해도 안 되는 건 매한가지였다.
```
➜ pip install pwntools
  error: subprocess-exited-with-error
  
  × python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [3 lines of output]
      running bdist_wheel
      running build
      error: [Errno 2] No such file or directory: '/private/var/folders/6b/nrw239cs5hqfrl7m0xk96zwc0000gn/T/pip-install-7c2tjrc7/unicorn_5d9cf0ade48441adbdd3a12fd00cab19/../../include/unicorn'
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for unicorn
  Running setup.py clean for unicorn
Failed to build unicorn
Installing collected packages: unicorn, sortedcontainers, pyserial, pyelftools, certifi, urllib3, six, pysocks, pyparsing, pygments, pycparser, psutil, plumbum, MarkupSafe, intervaltree, idna, charset-normalizer, capstone, rpyc, ropgadget, requests, python-dateutil, packaging, mako, colored-traceback, cffi, pynacl, cryptography, bcrypt, paramiko, pwntools
  Running setup.py install for unicorn ... error
  error: subprocess-exited-with-error
  
  × Running setup.py install for unicorn did not run successfully.
  │ exit code: 1
  ╰─> [5 lines of output]
      running install
      /opt/homebrew/Caskroom/miniforge/base/envs/sage-test/lib/python3.9/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
        warnings.warn(
      running build
      error: [Errno 2] No such file or directory: '/private/var/folders/6b/nrw239cs5hqfrl7m0xk96zwc0000gn/T/pip-install-7c2tjrc7/unicorn_5d9cf0ade48441adbdd3a12fd00cab19/../../include/unicorn'
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure

× Encountered error while trying to install package.
╰─> unicorn

note: This is an issue with the package mentioned above, not pip.
hint: See above for output from the failure.
```
에러를 찬찬히 읽어보니 `unicorn` 패키지에서 문제가 생긴 것을 알 수 있었다. 다행히도, `pip install unicorn`만 따로 하면 설치가 된다. 그런데 이번에는 정작 `pwntools`가 설치가 안 된다!! 이후로 삽질을 엄청나게 오래 했는데, `pwntools`를 먼저 설치한 다음 `sage`를 설치하니 정상적으로 설치가 되는 것을 알 수 있었다. 즉, 반드시 다음의 순서로 설치를 진행해야 한다.
```
pip install unicorn
pip install pwntools
conda install sage
```
왜인지는 나도 모르겠다. 🤷‍♂️ 또 까먹을까봐 일단 블로그에 적어 둔다.