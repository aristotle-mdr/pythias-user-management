from aristotle_mdr.apps import AristotleExtensionBaseConfig

class PythiasUserConfig(AristotleExtensionBaseConfig):
    name = 'pythias_user_management'
    verbose_name = "Pythias advanced user management extension"
    description = """
    Pythias adds extra management of users including:
    * lockouts for consecutive falures
    * limiting concurrent logins
    * assigning work tasks
    """
