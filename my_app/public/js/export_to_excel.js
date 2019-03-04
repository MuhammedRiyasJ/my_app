frappe.ui.form.on("Quotation", "refresh", function(frm) {
    frm.add_custom_button(__("Export to Excel"), function() {
        // When this button is clicked, do this
			var name = frm.doc.name;
			var item_name = [];
			var item_code = [];
			var qty = [];
			var rate = [];
			var amount = [];
            $.each(frm.doc.items || [], function(i, d) {
				item_name.push(d.item_name);
				 item_code.push(d.item_code);
				 qty.push(d.qty);
				 rate.push(d.net_rate);
				 amount.push(d.net_amount);
			});
		   frappe.call({
            		"method": "my_app.my_app.my.create_file",
            		args: {
                
					'name':name,
					'item_name':item_name,
					'qty':qty,
					'item_code':item_code,
					'rate':rate,
					'amount':amount
            		},
			 callback: function(r) {
                                console.log(r)
                                var file_url = r.message.file_name
                                if (file_url) {
                                        file_url = file_url.replace(/#/g, '%23');
                                }
                                window.open(file_url);
                     }

          
	    	});
    });
});
//  	var transaction_date = frm.doc.transaction_date;
		     // var valid_till = frm.doc.valid_till;
		     // var company = frm.doc.company;
		     // var customer = frm.doc.customer;
		     // var quotation_to = frm.doc.quotation_to;
		     // var lead = frm.doc.lead;
		     // var customer_address = frm.doc.customer_address;
		     // var address_display = frm.doc.address_display;
		     // var contact_person = frm.doc.contact_person;
		     // var contact_display = frm.doc.contact_display;
		     // var contact_mobile = frm.doc.contact_mobile;
		     // var contact_email = frm.doc.contact_email;
		     // var shipping_address_name = frm.doc.shipping_address_name;
		     // var shipping_address = frm.doc.shipping_address;
		     // var customer_group = frm.doc.customer_group;
		     // var territory = frm.doc.territory;
		     // var currency = frm.doc.currency;
		     // var selling_price_list = frm.doc.selling_price_list;
		     // var items = frm.doc.items;
		     // var total_qty = frm.doc.total_qty;
		     // var base_total = frm.doc.base_total;
		     // var base_net_total = frm.doc.base_net_total;
		     // var total = frm.doc.total;
		     // var net_total = frm.doc.net_total;
		     // var total_net_weight = frm.doc.total_net_weight;
		     // var taxes_and_charges = frm.doc.taxes_and_charges;
		     // var shipping_rule = frm.doc.shipping_rule;
		     // var taxes = frm.doc.taxes;
		     // var total_taxes_and_charges = frm.doc.total_taxes_and_charges;
		     // var apply_discount_on = frm.doc.apply_discount_on;
		     // var discount_amount = frm.doc.discount_amount;
		     // var base_grand_total = frm.doc.base_grand_total;
		     // var base_rounding_adjustment = frm.doc.base_rounding_adjustment;
		     // var grand_total = frm.doc.grand_total;
		     // var rounded_total = frm.doc.rounded_total;
		     // var in_words = frm.doc.in_words;
		     // var terms = frm.doc.terms;
		     // var status = frm.doc.status;
		     // var supplier_quotation = frm.doc.supplier_quotation;
		     // var opportunity = frm.doc.opportunity;

 //       			'transaction_date': transaction_date,
					// 'valid_till':valid_till,
					// 'company':company,
					// 'customer':customer,
					// 'quotation_to':quotation_to,
					// 'lead':lead,
					// 'customer_address':customer_address,
					// 'address_display':address_display,
					// 'contact_person':contact_person,
					// 'contact_display':contact_display,
					// 'contact_mobile':contact_mobile,
					// 'contact_email':contact_email,
					// 'shipping_address_name':shipping_address_name,
					// 'shipping_address':shipping_address,
					// 'customer_group':customer_group,
					// 'territory':territory,
					// 'currency':currency,
					// 'selling_price_list':selling_price_list,
					// 'items':items,
					// 'total_qty':total_qty,
					// 'base_total':base_total,
					// 'base_net_total':base_net_total,
					// 'total':total,
					// 'net_total':net_total,
					// 'total_net_weight':total_net_weight,
					// 'taxes_and_charges':taxes_and_charges,
					// 'shipping_rule':shipping_rule,
					// 'taxes':taxes,
					// 'total_taxes_and_charges':total_taxes_and_charges,
					// 'apply_discount_on':apply_discount_on,
					// 'discount_amount':discount_amount,
					// 'base_grand_total':base_grand_total,
					// 'base_rounding_adjustment':base_rounding_adjustment,
					// 'grand_total':grand_total,
					// 'rounded_total':rounded_total,
					// 'in_words':in_words,
					// 'terms':terms,
					// 'status':status,
					// 'supplier_quotation':supplier_quotation,
					// 'opportunity':opportunity