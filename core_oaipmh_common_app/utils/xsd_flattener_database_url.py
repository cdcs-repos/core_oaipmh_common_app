"""XSD Flattener Database or URL class
"""
from xml_utils.xsd_flattener.xsd_flattener_url import XSDFlattenerURL
from urlparse import urlparse
from core_main_app.components.template import api as template_api
from core_main_app.commons import exceptions


class XSDFlattenerDatabaseOrURL(XSDFlattenerURL):
    """
    Get the content of the dependency from the database or from the URL.
    """

    def __init__(self, xml_string, download_enabled=True):
        """Initializes the flattener

        Args:
            xml_string:
            download_enabled:
        """
        XSDFlattenerURL.__init__(self, xml_string=xml_string, download_enabled=download_enabled)

    def get_dependency_content(self, uri):
        """ Get the content of the dependency from the database or from the URL.
            1st: Directly from database
            2nd: Downloads the content found at the URL.
        Args:
            uri: Content URI.

        Returns:
            Content.

        """
        try:
            url = urlparse(uri)
            _id = url.query.split("=")[1]
            # TODO: Think about Type
            template = template_api.get(_id)
            content = template.content
        except (exceptions.DoesNotExist, exceptions.ModelError, Exception):
            content = super(XSDFlattenerDatabaseOrURL, self).get_dependency_content(uri)

        return content
