'''
Plugsy SDK - Exceptions
'''

class PluginsHomeNotFound(Exception):
    '''
    To be raised if the specified plugins home directory is not found
    '''

    def __init__(self, plugins_home_path):
        message = "The plugins home path at '%s' could not be found, or is not a valid directory" % plugins_home_path
        Exception.__init__(self, message)


class PluginAlreadyExists(Exception):
    '''
    To be raised if a user is trying to create a plugin, but the plugin already exists
    '''

    def __init__(self, plugin_name):
        message = "The plugin '%s' already exists" % plugin_name
        Exception.__init__(self, message)


class PluginCreationFailure(Exception):
    '''
    Generic exception to be raised when - for whatever reason - the plugin could not
    be created
    '''

    def __init__(self, name, message):
        message = "The plugin '%s' could not be created: %s" % (name, message)
        Exception.__init__(self, message)


class PluginTypeNotSet(Exception):
    '''
    To be raised if the user is trying to create a plugin without setting it as core or addon
    @todo Test
    '''

    def __init__(self, name):
        message = "The plugin type must be set before calling create()"
        Exception.__init__(self, message)

