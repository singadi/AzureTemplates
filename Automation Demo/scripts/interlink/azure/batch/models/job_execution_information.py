# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobExecutionInformation(Model):
    """Contains information about the execution of a job in the Azure Batch
    service.

    :param start_time: The start time of the job.
    :type start_time: datetime
    :param end_time: The completion time of the job. This property is set
     only if the job is in the completed state.
    :type end_time: datetime
    :param pool_id: The id of the pool to which this job is assigned.
    :type pool_id: str
    :param scheduling_error: Details of any error encountered by the service
     in starting the job.
    :type scheduling_error: :class:`JobSchedulingError
     <azure.batch.models.JobSchedulingError>`
    :param terminate_reason: A string describing the reason the job ended.
    :type terminate_reason: str
    """ 

    _validation = {
        'start_time': {'required': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'pool_id': {'key': 'poolId', 'type': 'str'},
        'scheduling_error': {'key': 'schedulingError', 'type': 'JobSchedulingError'},
        'terminate_reason': {'key': 'terminateReason', 'type': 'str'},
    }

    def __init__(self, start_time, end_time=None, pool_id=None, scheduling_error=None, terminate_reason=None):
        self.start_time = start_time
        self.end_time = end_time
        self.pool_id = pool_id
        self.scheduling_error = scheduling_error
        self.terminate_reason = terminate_reason
