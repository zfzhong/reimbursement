#!/usr/bin/env python3

import json

class PurchaseItem:
    def __init__(self, item, purpose, date, amount, receipt, pdf, category, status, updated):
        self.item = item
        self.purpose = purpose
        self.date = date
        self.amount = amount
        self.receipt = receipt
        self.pdf = pdf
        self.category = category
        self.status = status
        self.updated = updated

    def html(self):
        s = []
        s.append("\t\t<tr>\n")
        s.append("\t\t<td>%s</td>\n" % self.item)
        s.append("\t\t<td>%s</td>\n" % self.purpose)
        s.append("\t\t<td>%s</td>\n" % self.date)
        s.append("\t\t<td>%s</td>\n" % self.amount)
        s.append('\t\t<td><img src="%s"/><br/><a href="%s">PDF</a></td>\n' % (self.receipt, self.pdf))
        s.append("\t\t<td>%s</td>\n" % self.category)
        s.append("\t\t<td>%s</td>\n" % self.status)
        s.append("\t\t<td>%s</td>\n" % self.updated)
        s.append("\t\t</tr>\n")

        return "".join(s)
    

def j2h(filename):
    data = None
    with open(filename, "r") as f:
        data = json.load(f)

    s = []
    items = (data["items"])
    for x in items:
        p = PurchaseItem(x["item"], x["purpose"], x["date"], x["amount"], x["receipt"], x["pdf"], x["category"], x["status"], x["updated"])
        s.append(p.html())

    return "".join(s)


    
import sys
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python", sys.argv[0], "<json_file>")
        sys.exit(1)


    filename = sys.argv[1]
    
    s = j2h(filename)

    f = open("list_framework.html")
    lines = f.readlines()

    print("".join(lines) % s)
