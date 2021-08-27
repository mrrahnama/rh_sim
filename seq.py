import pandas as pd
from server import MarketSimulation
import random


def menu():
    contin = "yes"
    while (contin == "yes"):
        print("enter range of numbers (a,b) :")
        a = int(input("enter a = "))
        b = int(input("enter b = "))
        alist = list(range(a, b + 1))
        for i in alist:
            print(i, end=' ')
        order = input("\nselect order : 'des'  or 'asc'")
        if (order == "des"):
            alist.reverse()
        for i in alist:
            if (i % 2 != 0):
                print(i, end=' ')
        contin = input("\ncontinue? 'yes' or 'no'\n ")


# menu()
import dill
import numpy as np
from Model import Product, Market


class AssortmentModel:
    n = 0  # number of products
    m = 0  # number of customer types
    lam = np.zeros(m)
    profit = np.zeros(n)
    products = np.zeros(n)
    pl = np.zeros((m, n))
    alpha = np.zeros(n)
    alpha2 = np.zeros((m, n))
    file_path = ''
    file_name = ''


def import_seller(filepath, AssortmentModelobj, msim=None):
    dfs = pd.read_excel(filepath, sheet_name="Offer set", engine='openpyxl')
    if msim is None:
        msim = MarketSimulation()
    elif not isinstance(msim, MarketSimulation):
        return None
    data = dfs.to_dict()[1]
    productnames = []
    for row in data.keys():
        if data[row] == 1:
            productnames.append(row + 1)
    inventory = []
    item = {}

    if isinstance(AssortmentModelobj, AssortmentModel):
        for pn in productnames:
            item["name"] = pn
            item["minvalue"] = AssortmentModelobj.profit[int(pn) - 1]
            item["count"] = 10000
            inventory.append(dict(item))
        return msim.create_seller(0.0, msim.create_inventory(inventory), "opt_assortment_seller")

    return None
    # todo change create_inventory function from dict to list


def import_customertypes(assortmentModelobj, msim=None,population_size=1000):
    budget = 1000
    customerlist = []
    if msim is None:
        msim = MarketSimulation()
    elif not isinstance(msim, MarketSimulation):
        return None
    if isinstance(assortmentModelobj, AssortmentModel):
        sum=np.sum(assortmentModelobj.lam)

        for nameid in range(assortmentModelobj.m):
            customerlist.append(
                msim.create_customer_type(str(nameid), 1, {k: budget for k in assortmentModelobj.pl[nameid]},
                                          int(assortmentModelobj.lam[nameid] * population_size), 0.9))
    return customerlist


def create_random_invrntory(assortmentModelobj, msim=None, lam_no_product=5):
    if msim is None:
        msim = MarketSimulation()
    elif not isinstance(msim, MarketSimulation):
        return None
    if isinstance(assortmentModelobj, AssortmentModel):
        list_id = {}
        i = 0
        # no_product = min(np.random.poisson(lam=lam_no_product),assortmentModelobj.n)
        no_product = lam_no_product
        while len(list_id) < no_product:
            r = random.randint(1, assortmentModelobj.n)
            if r not in list_id.keys():
                list_id[r] = {"name": r, "minvalue": assortmentModelobj.profit[int(r) - 1], "count": 10000}
        return list(list_id.values())


def create_random_seller_for_assortment(AssortmentModelobj, lam_no_product=5, msim=None):
    if msim is None:
        msim = MarketSimulation()
    elif not isinstance(msim, MarketSimulation):
        return None
    if isinstance(AssortmentModelobj, AssortmentModel):
        return msim.create_seller(0.0, msim.create_inventory(create_random_invrntory(AssortmentModelobj, msim, lam_no_product)),"random_assortment_seller")


fileName = r"C:\SSD\Uni\Thesis\mr eskandari\pref_\model_200x50_1.pickle"
products = r"C:\SSD\Uni\Thesis\mr eskandari\inventory\model_200x50_1\23\result_023.xlsx"
with open(fileName, 'rb') as filehandler:
    AssortmentModelobj1 = dill.load(filehandler)
simobj = MarketSimulation()
customertypes = import_customertypes(AssortmentModelobj1, msim=simobj,population_size=10000)
assortmentseller = import_seller(products, AssortmentModelobj1, msim=simobj)
sellerlist = []
sellerlist.append(assortmentseller)
for i in range(5):
    # sellerlist.append(create_random_seller_for_assortment(AssortmentModelobj1,int(np.random.poisson(0.6*AssortmentModelobj1.n)),simobj))
    sellerlist.append(create_random_seller_for_assortment(AssortmentModelobj1,len(assortmentseller.inventory),simobj))
print("procces finished")
simobj.set_market_capacity(150)
simobj.set_max_days(1)
simobj.report_path = "C:/SSD/Uni/Thesis/Source/main/simulator/reports/"
i = 1
for seller in sellerlist:
    seller.unique_id=i
    simobj.add_seller(seller)
    i += 1
i=0
for custype in customertypes:
    if i<200:
        simobj.add_customer_type(custype)
        i+=1
    else :
        break
simobj.run(visual=False)
# for i in range(simobj.simulation_time):

