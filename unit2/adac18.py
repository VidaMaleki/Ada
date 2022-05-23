# $100.00 for each guitar sold
# $200.00 for each violin sold
# $150.00 for each piano broken

# def calculate_store_profits(guitars_sold, violins_sold, pianos_broke):
#     # variables/parameters
#     store_1 = {'guitars_sold': 12, 'violins_sold': 1, 'pianos_broke': 6}
#     store_2 = {'guitars_sold': 20, 'violins_sold': 0, 'pianos_broke': 5}
#     store_3 = {'guitars_sold': 10, 'violins_sold': 5, 'pianos_broke': 5}
#     guitar_net_gain = 100.00
#     violin_net_gain = 200.00
#     piano_net_loss = -150.00

#     store_1 = {'guitars_sold': 12(guitar_net_gain), 'violins_sold': 1(violin_net_gain), 'pianos_broke': 6(piano_net_loss)}
#     for i in store_1:
#         print("Item = %s, Money = %d" %(i, store_1[i]))

#     store_2 = {'guitars_sold': 20(guitar_net_gain), 'violins_sold': 0(violin_net_gain), 'pianos_broke': 5(piano_net_loss)}
#     for i in store_2:
#         print("Item = %s, Money = %d" %(i, store_2[i]))

#     store_3 = {'guitars_sold': 10(guitar_net_gain), 'violins_sold': 5(violin_net_gain), 'pianos_broke': 5*(piano_net_loss)}
#     for i in store_3:
#         print("Item = %s, Money = %d" %(i, store_3[i]))

# #print('Store #' + str(store_id) + ' made $' + str(income_generated) + ' after costs +$' + str(guitars_sold) + \
# #' from guitars +$' + str(violins_sold) + ' from violins -$' + str(pianos_broke) + ' from pianos.')

# #output: Store #2 made $1250.00 after costs +$2000.00 from guitars +$0.00 from violins -$750.00 from pianos.



guitars_sold = [12, 20, 10]
violins_sold = [1, 0, 5]
pianos_broke = [6, 5, 5]

guitars_price = 100.00
violins_price = 200.00
pianos_price = 150.00


def calculate_store_profits(guitars_sold, violins_sold, pianos_broke):

    def guitar_calculation(store_id):
        return guitars_sold[store_id] * guitars_price
        
    def violin_calculation(store_id):
        return violins_sold[store_id] * violins_price
        
    def piano_broke_calculation(store_id):
        return pianos_broke[store_id] * pianos_price
    
    def total_per_store(store_id):
        return guitar_calculation(store_id) + violin_calculation(store_id) - piano_broke_calculation(store_id)
    
    def total_all_stores():
        total = 0
        for store in range(len(guitars_sold)):
            total += total_per_store(store)
        return total 
    
    for store_id in range(len(guitars_sold)):
        print(f"Store #{store_id +1} made ${total_per_store(store_id)} after costs +${guitar_calculation(store_id)} from guitars +${violin_calculation(store_id)}from violins -${piano_broke_calculation(store_id)} from pianos.")
    print(f"total for all stores is {total_all_stores()}")
        


calculate_store_profits(guitars_sold, violins_sold, pianos_broke)        
