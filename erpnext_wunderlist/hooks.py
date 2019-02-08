# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_wunderlist"
app_title = "Erpnext Wunderlist"
app_publisher = "Techlift"
app_description = "This app is to integrate ERPNext Project and Task with Wunderslit"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "palash@techlift.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_wunderlist/css/erpnext_wunderlist.css"
# app_include_js = "/assets/erpnext_wunderlist/js/erpnext_wunderlist.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_wunderlist/css/erpnext_wunderlist.css"
# web_include_js = "/assets/erpnext_wunderlist/js/erpnext_wunderlist.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_wunderlist.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_wunderlist.install.before_install"
# after_install = "erpnext_wunderlist.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_wunderlist.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_wunderlist.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_wunderlist.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_wunderlist.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_wunderlist.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_wunderlist.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_wunderlist.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_wunderlist.event.get_events"
# }

