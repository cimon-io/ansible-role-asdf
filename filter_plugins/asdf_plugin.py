# -*- coding: utf-8 -*-
def get_asdf_global_version(asdf_plugin_item):
    list_version = list(set(asdf_plugin_item['versions']).difference(set(asdf_plugin_item.get('delete_versions', []))))
    list_version.sort()
    return asdf_plugin_item.get('global', list_version[0])

class FilterModule(object):

    def filters(self):
        return {
            'get_asdf_global_version': get_asdf_global_version
        }
