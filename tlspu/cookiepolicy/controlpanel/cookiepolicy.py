# -*- coding:utf-8 -*-

from zope.schema import Bool
from zope.schema import TextLine
from zope.schema import Text
from zope.component import adapts
from zope.interface import Interface
from zope.interface import implements

from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFPlone.utils import getToolByName
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase

from plone.app.controlpanel.form import ControlPanelForm

from plone.fieldsets.fieldsets import FormFieldsets

from tlspu.cookiepolicy import TCPMessageFactory as _


class ICookiePolicySchema(Interface):
    """ Global statusmessage overlay configuration """

    TCP_enabled = Bool(
        title=_(u"Enable Global statusmessage overlay"),
        default=True,
        required=False,
    )

    TCP_title = TextLine(
        title=_(u'Title'),
        default=_(u'This Site Uses Cookies'),
        description=_(u'help_tcp_title',
            default=u"Enter the title for the Global statusmessage overlay",
        ),
        required=True,
    )

    TCP_message = Text(
        title=_(u'Message'),
        description=_(
            u'help_tcp_message',
            default=(u"Enter the message for the Global statusmessage overlay. This may "
                     u"contain HTML"),
        ),
        required=True,
    )

    TCP_submit_button = TextLine(
        title=_(u'Submit button'),
        default=_(u'OK'),
        description=_(u'help_tcp_submit_button',
            default=u"Enter the title for the Global statusmessage overlay submit button.",
        ),
        required=True,
    )


class BaseControlPanelAdapter(SchemaAdapterBase):
    """ Base control panel adapter """

    def __init__(self, context):
        super(BaseControlPanelAdapter, self).__init__(context)
        portal_properties = getToolByName(context, 'portal_properties')
        self.context = portal_properties.tlspu_cookiepolicy_properties


class CookiePolicyControlPanelAdapter(BaseControlPanelAdapter):
    """ Cookie Policy control panel adapter """
    adapts(IPloneSiteRoot)
    implements(ICookiePolicySchema)

    TCP_enabled = ProxyFieldProperty(ICookiePolicySchema['TCP_enabled'])
    TCP_title = ProxyFieldProperty(ICookiePolicySchema['TCP_title'])
    TCP_message = ProxyFieldProperty(ICookiePolicySchema['TCP_message'])
    TCP_submit_button = ProxyFieldProperty(ICookiePolicySchema['TCP_submit_button'])

baseset = FormFieldsets(ICookiePolicySchema)
baseset.id = 'cookiepolicy'
baseset.label = _(u'Global statusmessage overlay')


class CookiePolicyControlPanel(ControlPanelForm):
    """ """
    form_fields = FormFieldsets(baseset)

    label = _('Global statusmessage overlay settings')
    description = _('Configure settings for Global Statusmessage overlay.')
    form_name = _('Global statusmessage overlay')
