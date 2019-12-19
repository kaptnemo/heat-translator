#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from translator.hot.translate_node_templates import _generate_type_map
from translator.tests.base import TestCase


class TranslateNodeTemplatesTest(TestCase):

    def test_generate_type_map(self):

        expected_type_list = [
            'tosca.nodes.BlockStorage',
            'tosca.nodes.Compute',
            'tosca.nodes.DBMS',
            'tosca.nodes.Database',
            'tosca.nodes.ObjectStorage',
            'tosca.nodes.SoftwareComponent',
            'tosca.nodes.WebApplication',
            'tosca.nodes.WebServer',
            'tosca.nodes.network.FloatingIP',
            'tosca.nodes.network.Network',
            'tosca.nodes.network.Port',
            'tosca.policies.Monitoring',
            'tosca.policies.Placement',
            'tosca.policies.Reservation',
            'tosca.policies.Scaling',
            'tosca.policies.Scaling.Cluster'
        ]
        actual_type_list = list(_generate_type_map())

        self.assertItemsEqual(expected_type_list, actual_type_list)