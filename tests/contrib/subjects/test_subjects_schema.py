# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Northwestern University.
#
# Invenio-Vocabularies is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Affiliations Marshmallow schema tests."""
from copy import copy

import pytest
from marshmallow import ValidationError

from invenio_vocabularies.contrib.subjects.schema import SubjectSchema


def test_valid_full(subject_full_data):
    loaded = SubjectSchema().load(subject_full_data)
    assert subject_full_data == loaded


def test_invalid_missing_field(subject_full_data):
    # no id
    invalid = copy(subject_full_data)
    del invalid["id"]
    with pytest.raises(ValidationError):
        SubjectSchema().load(invalid)

    # no scheme
    invalid = copy(subject_full_data)
    del invalid["scheme"]
    with pytest.raises(ValidationError):
        SubjectSchema().load(invalid)

    # no subject
    invalid = copy(subject_full_data)
    del invalid["subject"]
    with pytest.raises(ValidationError):
        SubjectSchema().load(invalid)
