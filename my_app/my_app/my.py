
from __future__ import unicode_literals
import frappe
from frappe.utils import flt, cstr,today,now,now_datetime
from frappe import msgprint, _
import os

# @frappe.whitelist()
# def create_file(transaction_date = '',valid_till = '',company='',customer='',quotation_to='',lead='',customer_address='',address_display='',contact_person='',contact_display='',contact_mobile='',contact_email='',shipping_address_name='',shipping_address='',customer_group='',territory='',currency='',selling_price_list='',items='',total_qty='',base_total='',base_net_total='',total='',net_total='',total_net_weight='',taxes_and_charges='',shipping_rule='',taxes='',total_taxes_and_charges='',apply_discount_on='',discount_amount='',base_grand_total='',base_rounding_adjustment='',grand_total='',rounded_total='',in_words='',terms='',status='',supplier_quotation='',opportunity=''):
	
# 	filters = {'transaction_date':transaction_date,'valid_till':valid_till,'company':company}

# 	curr_date = today()
# 	fname = "Quotation"+frappe.utils.formatdate(today(),'YYMMd')+now_datetime().strftime('%H%M%S')+".xlsx"
# 	save_path = 'site1.local/private/files'

#         #save_path = 'site1.local/private/files'	
# 	file_name = os.path.join(save_path, fname)
# 	ferp = frappe.new_doc("File")
# 	ferp.file_name = fname
# 	ferp.folder = "Home"
# 	ferp.is_private = 1
# 	ferp.file_url = "/private/files/"+fname
# 	f= open(file_name,"w+")
# 	for item in items:
# 		itm = [str(i) for i in item]
# 		file_string = (','.join(itm))+'\n'
# 		f.write(file_string)
# 	data = "Company Name"+'\t'+"Date"+'\n'+(company)+'\t'+(transaction_date)+'\t'+(customer)+'\t'+(quotation_to)+'\t'+(lead)+'\t'+(customer_address)+'\t'+(address_display)+'\t'+(contact_person)+'\t'+(contact_display)+'\t'+(contact_mobile)+'\t'+(contact_email)+'\t'+(shipping_address_name)+'\t'+(shipping_address)+'\t'+(customer_group)+'\t'+(territory)+'\t'+(currency)+'\t'+(selling_price_list)+'\t'+(total_qty)+'\t'+(base_total)+'\t'+(base_net_total)+'\t'+(total)+'\t'+(net_total)+'\t'+(total_net_weight)+'\t'+(taxes_and_charges)+'\t'+(shipping_rule)+'\t'+(taxes)+'\t'+(total_taxes_and_charges)+'\t'+(apply_discount_on)+'\t'+(discount_amount)+'\t'+(base_grand_total)+'\t'+(base_rounding_adjustment)+'\t'+(grand_total)+'\t'+(rounded_total)+'\t'+(in_words)+'\t'+(terms)+'\t'+(status)+'\t'+(supplier_quotation)+'\t'+(opportunity)
# 	f.write(data)
# 	ferp.save()
# 	f.close()
# 	return {'file_name':"/private/files/"+fname}


@frappe.whitelist()
def create_file(name ='',item_name='',item_code='',qty='',rate='',amount=''):
	qtn_data = frappe.db.sql("""select company,customer from `tabQuotation` where name=%s""",(name))[0]
	company = qtn_data[0]
	customer = qtn_data[1]
	curr_date = today()
	fname = "Quotation"+name+".xlsx"
	save_path = 'site1.local/private/files'

        #save_path = 'site1.local/private/files'	
	file_name = os.path.join(save_path, fname)
	ferp = frappe.new_doc("File")
	ferp.file_name = fname
	ferp.folder = "Home"
	ferp.is_private = 1
	ferp.file_url = "/private/files/"+fname
	f= open(file_name,"w+")
	print(item_name[1])
	data = "Company Name"+'\t'+"Date"+'\t'+company+'\t'+customer+'\t'+item_name
	f.write(data)
	ferp.save()
	f.close()
	return {'file_name':"/private/files/"+fname}

