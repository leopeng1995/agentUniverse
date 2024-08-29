# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/8/27 15:53
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: plugin_dto.py
from typing import Optional, List

from pydantic import BaseModel, Field


class PluginDTO(BaseModel):
    id: str = Field(description="ID")
    nickname: Optional[str] = Field(description="plugin nickname", default="")
    avatar: Optional[str] = Field(description="plugin avatar path", default="")
    toolset: Optional[List[str]] = Field(description="plugin toolset", default=[])
    openapi_desc: Optional[str] = Field(description="plugin openapi schema", default="")
