# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "my_app"
app_title = "My App"
app_publisher = "riyas"
app_description = "Export to excel"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "riyaspangode@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/my_app/css/my_app.css"
# app_include_js = "/assets/my_app/js/my_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/my_app/css/my_app.css"
# web_include_js = "/assets/my_app/js/my_app.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Quotation" : "public/js/export_to_excel.js","Sales Invoice" : "public/js/sales_invoice.js"}
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
# get_website_user_home_page = "my_app.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "my_app.install.before_install"
# after_install = "my_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "my_app.notifications.get_notification_config"

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
# 		"my_app.tasks.all"
# 	],
# 	"daily": [
# 		"my_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"my_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"my_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"my_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "my_app.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "my_app.event.get_events"
# }

