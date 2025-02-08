import frappe

@frappe.whitelist()
def get_clusters():
    return frappe.get_all("democluster", fields=["name", "country"])

@frappe.whitelist()
def create_cluster(name, country):
    doc = frappe.get_doc({
        "doctype": "demoCluster",
        "name": name,
        "country": country
    })
    doc.insert()
    return doc

@frappe.whitelist()
def update_cluster(cluster_name, country):
    doc = frappe.get_doc("demoCluster", cluster_name)
    doc.country = country
    doc.save()
    return doc

@frappe.whitelist()
def delete_cluster(cluster_name):
    frappe.delete_doc("demoCluster", cluster_name)
    return {"message": "Cluster deleted"}
