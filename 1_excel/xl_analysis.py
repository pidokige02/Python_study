from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, column_index_from_string
from copy import copy, deepcopy
import sys

file_name = "osprey_issues_master.xlsx"
txt = ""

if len(sys.argv) == 1:
    txt = "running : Python xl_analysis.py {} ".format(file_name)
    print(txt) 
elif len(sys.argv) == 2:
    file_name = sys.argv[1]
    txt = "running : Python xl_analysis.py {} ".format(file_name)
    print(txt) 
else:  
    print("Usage : Python xl_analysis.py file_name.xlsx")
    sys.exit()

wb_src = load_workbook(file_name)
# ws_srcs = []  # using list 

print(wb_src.sheetnames)

# getting target worksheet for analysis
# ws_srcs.append(wb_src[ws_src.title])
ws_src = wb_src[wb_src.sheetnames[1]]
ws_summary = wb_src[wb_src.sheetnames[0]]

print(ws_src)
print(ws_summary)
print(ws_src.title)

txt = "=COUNTA('{}'!A2:A3000)".format(ws_src.title)
ws_summary["B2"] = txt

#NC from ALL SPR
txt = "=COUNTIF('{0}'!J2:J3000,\"=NC - Design Non-Conformance\")".format(ws_src.title)
ws_summary["B3"] = txt

#NC Major from ALL SPR
txt = "=COUNTIFS('{0}'!J2:J3000,\"=NC - Design Non-Conformance\", '{0}'!AB2:AB3000, \"=Major\")".format(ws_src.title)
ws_summary["B4"] = txt


#NC Minor from ALL SPR
txt = "=COUNTIFS('{0}'!J2:J3000,\"=NC - Design Non-Conformance\", '{0}'!AB2:AB3000, \"=Minor\")".format(ws_src.title)
ws_summary["B5"] = txt

#NC Not Scope from ALL SPR
txt = "=COUNTIFS('{0}'!J2:J3000,\"=NC - Design Non-Conformance\", '{0}'!AB2:AB3000, \"=Not Scope\")".format(ws_src.title)
ws_summary["B6"] = txt

#NC etc from ALL SPR
txt = "=COUNTIFS('{0}'!J2:J3000,\"=NC - Design Non-Conformance\", '{0}'!AB2:AB3000, \"=Not Scope\")".format(ws_src.title)
ws_summary["B7"] = txt

#IO from ALL SPR
txt = "=COUNTIFS('{0}'!J2:J3000,\"=IO - Improvement Opportunity\")".format(ws_src.title)
ws_summary["B8"] = txt

# Not Started from  ALL SPR
txt = "=COUNTIFS('{0}'!M2:M3000,\"=Submitted\")\
+COUNTIFS('{0}'!M2:M3000,\"=Accepted\")\
+COUNTIFS('{0}'!M2:M3000,\"=In Review\")\
+COUNTIFS('{0}'!M2:M3000,\"=Postponed\")".format(ws_src.title)
ws_summary["B9"] = txt

#NC for Not Started
txt = "=COUNTIFS('{0}'!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS('{0}'!M2:M3000,\"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS('{0}'!M2:M3000,\"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS('{0}'!M2:M3000,\"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")".format(ws_src.title)
ws_summary["B10"] = txt

#NC Major for Not Started
txt = "=COUNTIFS('{0}'!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\", '{0}'!AB2:AB3000, \"=Major\")\
+COUNTIFS('{0}'!M2:M3000,\"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS('{0}'!M2:M3000,\"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS('{0}'!M2:M3000,\"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")".format(ws_src.title)
ws_summary["B11"] = txt

#NC Minor for Not Started
txt = "=COUNTIFS('{0}'!M2:M3000,\"=Submitted\", '{0}'!J2:J3000, \"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000, \"=Minor\")\
+COUNTIFS('{0}'!M2:M3000,\"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000, \"=Minor\")\
+COUNTIFS('{0}'!M2:M3000,\"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000, \"=Minor\")\
+COUNTIFS('{0}'!M2:M3000,\"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000, \"=Minor\")".format(ws_src.title)
ws_summary["B12"] = txt

#NC Not Scope for Not Started
txt = "=COUNTIFS('{0}'!M2:M3000,\"=Submitted\",'{0}'!J2:J3000, \"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS('{0}'!M2:M3000,\"=Accepted\",'{0}'!J2:J3000, \"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000, \"=Not Scope\")\
+COUNTIFS('{0}'!M2:M3000,\"=In Review\",'{0}'!J2:J3000, \"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000, \"=Not Scope\")\
+COUNTIFS('{0}'!M2:M3000,\"=Postponed\",'{0}'!J2:J3000, \"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000, \"=Not Scope\")".format(ws_src.title)
ws_summary["B13"] = txt

#NC etc for Not Started 
txt = "=COUNTIFS('{0}'!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000, \"=''\")\
+COUNTIFS('{0}'!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000, \"=''\")\
+COUNTIFS('{0}'!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000, \"=''\")\
+COUNTIFS('{0}'!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000, \"=''\")".format(ws_src.title)
ws_summary["B14"] = txt

#IO for Not Strated
txt = "=COUNTIFS('{0}'!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS('{0}'!M2:M3000,\"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS('{0}'!M2:M3000,\"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS('{0}'!M2:M3000,\"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")".format(ws_src.title)
ws_summary["B15"] = txt


# In Progress from ALL SPR
txt = "=COUNTIFS('{0}'!M2:M3000,\"=In Progress\")".format(ws_src.title)
ws_summary["B16"] = txt

#NC for In Progress 
txt = "=COUNTIFS('{0}'!M2:M3000,\"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")".format(ws_src.title)
ws_summary["B17"] = txt

#NC Major for In Progress 
txt = "=COUNTIFS('{0}'!M2:M3000,\"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\", '{0}'!AB2:AB3000,\"=Major\")".format(ws_src.title)
ws_summary["B18"] = txt

#NC Minor for In Progress 
txt = "=COUNTIFS('{0}'!M2:M3000,\"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\", '{0}'!AB2:AB3000,\"=Minor\")".format(ws_src.title)
ws_summary["B19"] = txt

#NC Not Scope for In Progress 
txt = "=COUNTIFS('{0}'!M2:M3000,\"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\", '{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title)
ws_summary["B20"] = txt

#NC etc for In Progress 
txt = "=COUNTIFS('{0}'!M2:M3000,\"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\", '{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title)
ws_summary["B21"] = txt


#IO for In Progress 
txt = "=COUNTIFS('{0}'!M2:M3000,\"=In Progress\" ,'{0}'!J2:J3000,\"IO - Improvement Opportunity\")".format(ws_src.title)
ws_summary["B22"] = txt


#Resolved 
txt = "=COUNTIFS('{0}'!M2:M3000,\"=Resolved\")".format(ws_src.title)
ws_summary["B23"] = txt


#Verified 
txt = "=COUNTIFS('{0}'!M2:M3000,\"=Verified\")".format(ws_src.title)
ws_summary["B24"] = txt


#Closed 
txt = "=COUNTIFS('{0}'!M2:M3000,\"=Closed\")".format(ws_src.title)
ws_summary["B25"] = txt



# total SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\")   \
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\")       \
+COUNTIFS({0}!N2:N3000,\"=han il.lee\")       \
+COUNTIFS({0}!N2:N3000,\"=ho.lee\")           \
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\")      \
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\")      \
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\")     \
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\")     \
+COUNTIFS({0}!N2:N3000,\"=youjin.na\")        \
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\")      \
+COUNTIFS({0}!N2:N3000,\"=heejin.na\")".format(ws_src.title)
ws_summary["C2"] = txt

# NC SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")".format(ws_src.title)
ws_summary["C3"] = txt

# NC Major SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\" ,'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")".format(ws_src.title)
ws_summary["C4"] = txt

# NC Minor SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\" ,'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")".format(ws_src.title)
ws_summary["C5"] = txt

# NC Not Scope SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\" ,'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title)
ws_summary["C6"] = txt

# NC etc SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\" ,'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title)
ws_summary["C7"] = txt

# IO  SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")".format(ws_src.title)
ws_summary["C8"] = txt

# Not Started SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000,\"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Postponed\")".format(ws_src.title)
ws_summary["C9"] = txt

# Not Started SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")".format(ws_src.title)
ws_summary["C10"] = txt

# Not Started Major SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")".format(ws_src.title)
ws_summary["C11"] = txt

# Not Started Minor SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")".format(ws_src.title)
ws_summary["C12"] = txt

# Not Started Not Scope SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title)
ws_summary["C13"] = txt

# Not Started etc SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title)
ws_summary["C14"] = txt

# Not Started IO SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")".format(ws_src.title)
ws_summary["C15"] = txt

# in Prog SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Progress\")".format(ws_src.title) 
ws_summary["C16"] = txt

# in Prog NC owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")".format(ws_src.title) 
ws_summary["C17"] = txt

# in Prog NC Major owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")".format(ws_src.title) 
ws_summary["C18"] = txt


# in Prog NC Minor owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")".format(ws_src.title) 
ws_summary["C19"] = txt

# in Prog NC Not Scope owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title) 
ws_summary["C20"] = txt


# in Prog NC etc owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title) 
ws_summary["C21"] = txt

# in Prog IO owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000, \"=In Progress\" ,'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")".format(ws_src.title) 
ws_summary["C22"] = txt

# Resolved SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000,\"=Resolved\") \
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000,\"=Resolved\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000,\"=Resolved\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000,\"=Resolved\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000,\"=Resolved\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000,\"=Resolved\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000,\"=Resolved\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000,\"=Resolved\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000,\"=Resolved\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000,\"=Resolved\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000,\"=Resolved\")".format(ws_src.title) 
ws_summary["C23"] = txt

# Verified SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000,\"=Verified\") \
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000,\"=Verified\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000,\"=Verified\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000,\"=Verified\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000,\"=Verified\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000,\"=Verified\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000,\"=Verified\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000,\"=Verified\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000,\"=Verified\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000,\"=Verified\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000,\"=Verified\")".format(ws_src.title) 
ws_summary["C24"] = txt

# closd SPRs owned by s/w team
txt = "=COUNTIFS({0}!N2:N3000,\"=dongyoung.choi\",{0}!M2:M3000,\"=Closed\") \
+COUNTIFS({0}!N2:N3000,\"=taeyang.an\",{0}!M2:M3000,\"=Closed\")\
+COUNTIFS({0}!N2:N3000,\"=han il.lee\",{0}!M2:M3000,\"=Closed\")\
+COUNTIFS({0}!N2:N3000,\"=ho.lee\",{0}!M2:M3000,\"=Closed\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.jung\",{0}!M2:M3000,\"=Closed\")\
+COUNTIFS({0}!N2:N3000,\"=doo je.sung\",{0}!M2:M3000,\"=Closed\")\
+COUNTIFS({0}!N2:N3000,\"=jin ha.hwang\",{0}!M2:M3000,\"=Closed\")\
+COUNTIFS({0}!N2:N3000,\"=youngdug.kim\",{0}!M2:M3000,\"=Closed\")\
+COUNTIFS({0}!N2:N3000,\"=youjin.na\",{0}!M2:M3000,\"=Closed\")\
+COUNTIFS({0}!N2:N3000,\"=kyudong.kim\",{0}!M2:M3000,\"=Closed\")\
+COUNTIFS({0}!N2:N3000,\"=heejin.na\",{0}!M2:M3000,\"=Closed\")".format(ws_src.title) 
ws_summary["C25"] = txt


# total SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\")".format(ws_src.title)
ws_summary["D2"] = txt

# total NC SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")".format(ws_src.title)
ws_summary["D3"] = txt

# total NC Major SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")".format(ws_src.title)
ws_summary["D4"] = txt

# total NC Minor SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")".format(ws_src.title)
ws_summary["D5"] = txt

# total NC Not Scope SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title)
ws_summary["D6"] = txt

# total NC etc SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title)
ws_summary["D7"] = txt

# total IO SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")".format(ws_src.title)
ws_summary["D8"] = txt


# Not Started SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000,\"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Postponed\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Submitted\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Accepted\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Review\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Postponed\")".format(ws_src.title)
ws_summary["D9"] = txt

# Not Started NC SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")".format(ws_src.title)
ws_summary["D10"] = txt

# Not Started NC Major SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")".format(ws_src.title)
ws_summary["D11"] = txt

# Not Started NC Minor SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")".format(ws_src.title)
ws_summary["D12"] = txt

# Not Started NC Not Scope SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title)
ws_summary["D13"] = txt

# Not Started NC etc SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title)
ws_summary["D14"] = txt


# Not Started IO SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000,\"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Submitted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Accepted\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Review\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")\
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Postponed\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")".format(ws_src.title)
ws_summary["D15"] = txt


# In Prog SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Progress\") \
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Progress\")".format(ws_src.title) 
ws_summary["D16"] = txt

# In Prog NC SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\") \
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\")".format(ws_src.title) 
ws_summary["D17"] = txt

# In Prog NC Major SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\") \
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Major\")".format(ws_src.title) 
ws_summary["D18"] = txt

# In Prog NC Minor SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\") \
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Minor\")".format(ws_src.title) 
ws_summary["D19"] = txt

# In Prog NC Not Scope SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title) 
ws_summary["D20"] = txt

# In Prog NC etc SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\") \
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=NC - Design Non-Conformance\",'{0}'!AB2:AB3000,\"=Not Scope\")".format(ws_src.title) 
ws_summary["D21"] = txt

# In Prog io  SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\") \
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=In Progress\",'{0}'!J2:J3000,\"=IO - Improvement Opportunity\")".format(ws_src.title) 
ws_summary["D22"] = txt

# Resolved SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Resolved\") \
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Resolved\") \
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Resolved\") \
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Resolved\") \
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Resolved\") \
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Resolved\") \
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Resolved\")".format(ws_src.title) 
ws_summary["D23"] = txt

# Verified SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Verified\") \
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Verified\") \
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Verified\") \
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Verified\") \
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Verified\") \
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Verified\") \
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Verified\")".format(ws_src.title) 
ws_summary["D24"] = txt

# closed SPRs owned by system team
txt = "=COUNTIFS({0}!N2:N3000,\"=jihye.han\",{0}!M2:M3000, \"=Closed\") \
+COUNTIFS({0}!N2:N3000,\"=bong hyo.han\",{0}!M2:M3000, \"=Closed\") \
+COUNTIFS({0}!N2:N3000,\"=jae ha.hyun\",{0}!M2:M3000, \"=Closed\") \
+COUNTIFS({0}!N2:N3000,\"=jong gun.lee\",{0}!M2:M3000, \"=Closed\") \
+COUNTIFS({0}!N2:N3000,\"=jungho.kim\",{0}!M2:M3000, \"=Closed\") \
+COUNTIFS({0}!N2:N3000,\"=taeyun.kim\",{0}!M2:M3000, \"=Closed\") \
+COUNTIFS({0}!N2:N3000,\"=dongwoo.lee\",{0}!M2:M3000, \"=Closed\")".format(ws_src.title) 
ws_summary["D25"] = txt

wb_src.save(file_name)
wb_src.close()
