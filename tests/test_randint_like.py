# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import textwrap

import paddle
import pytest
from apibase import APIBase

obj = APIBase("torch.randint_like")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.zeros(3, 4, dtype=torch.float64)
        result = torch.randint_like(a, 0, 3)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.zeros(3, 4, dtype=torch.float64)
        result = torch.randint_like(a, 3)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.zeros(3, 4, dtype=torch.float64)
        result = torch.randint_like(a, 0, high=3, dtype=torch.float32, requires_grad=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.zeros(3, 4, dtype=torch.float64)
        flag = True
        result = torch.randint_like(a, low=0, high=3, dtype=torch.float32, requires_grad=flag)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.randint_like(torch.zeros(3, 4, dtype=torch.float64), 0, 3, dtype=torch.float32, requires_grad=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.randint_like(torch.zeros(3, 4, dtype=torch.float64), 0, 3, memory_format=torch.preserve_format, dtype=torch.float32, layout=torch.strided, device="cpu", pin_memory=False, requires_grad=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.randint_like(input=torch.zeros(3, 4), low=0, high=3, memory_format=torch.preserve_format, dtype=torch.float32, layout=torch.strided, device="cpu", pin_memory=False, requires_grad=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.randint_like(memory_format=torch.preserve_format, requires_grad=True, device="cpu", layout=torch.strided, dtype=torch.float32, high=3, low=0, input=torch.zeros(3, 4, dtype=torch.float64))
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_9():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.zeros(3, 4)
        high = 10
        result = torch.randint_like(x, high)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_10():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.zeros(3, 4)
        high = 10
        result = torch.randint_like(x, high=high, memory_format=torch.preserve_format, dtype=torch.float32, layout=torch.strided, device="cpu", pin_memory=False, requires_grad=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


@pytest.mark.skipif(
    condition=not paddle.device.is_compiled_with_cuda(),
    reason="can only run on paddle with CUDA",
)
def test_case_11():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.zeros(3, 4)
        high = 10
        result = torch.randint_like(input=x, high=high, memory_format=torch.preserve_format, dtype=torch.float32, layout=torch.strided, device="cpu", pin_memory=True, requires_grad=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)
