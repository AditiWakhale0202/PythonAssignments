import os

class PivotOperator():

    def process(list2):
        list1 = [ "MS-World_Allocation", "World_Allocation", "MS_Intermediate_Term_Bond", "Intermediate_Term_Bond", "MS_Short_Term_Bond", "Short_Term_Bond",
      "MS_Foreign_Large_Blend", "Foreign_Large_Blend", "MS_World_Stock", "World_Stock", "MS_High_Yield_Bond", "High_Yield_Bond", "MS_Nontraditional_Bond",
      "Nontraditional_Bond", "MS_Diversified_Emerging_Mkt", "Diversified_Emerging_Mkt", "MS_World_Bond", "World_Bond", "MS_Foreign_Large_Growth", "Foreign_Large_Growth", "MS_Multialternative",
      "Multialternative", "MS_Mid_Cap_Growth", "Mid_Cap_Growth", "MS_Small_Growth", "Small_Growth", "MS_Muni_National_Long", "Muni_National_Long", "MS_Mid_Cap_Blend", "Mid_Cap_Blend",
      "MS_Small_Value", "Small_Value", "MS_Real_Estate", "Real_Estate", "MS_Corporate_Bond", "Corporate_Bond", "MS_Intermediate_Government", "Intermediate_Government", "MS_Global_Real_Estate",
      "Global_Real_Estate", "MS_Europe_Stock", "Europe_Stock", "MS_Emerging_Markets_Bond", "Emerging_Markets_Bond", "MS_Short_Government", "Short_Government", "MS_Foreign_Small_Mid_Blend",
      "Foreign_Small_Mid_Blend", "MS_Pacific_Asia_ex_Japan_St", "Pacific_Asia_ex_Japan_St", "MS_Aggressive_Allocation", "Aggressive_Allocation", "MS_Conservative_Allocation",
      "Conservative_Allocation", "MS_Moderate_Allocation", "Moderate_Allocation", "MS_Retirement_Income", "Retirement_Income", "MS_Tactical_Allocation", "Tactical_Allocation",
      "MS_Bear_Market", "Bear_Market", "MS_Long_Short_Equity", "Long_Short_Equity", "MS_Managed_Futures", "Managed_Futures", "MS_Market_Neutral", "Market_Neutral",
      "MS_Multicurrency", "Multicurrency", "MS_Trading_Inverse_Commodit", "Trading_Inverse_Commodit", "MS_Trading_Inverse_Debt", "Trading_Inverse_Debt", "MS_Trading_Inverse_Equity",
      "Trading_Inverse_Equity", "MS_Trading_Leveraged_Commod", "Trading_Leveraged_Commod", "MS_Trading_Leveraged_Debt", "Trading_Leveraged_Debt", "MS_Trading_Leveraged_Equity",
      "Trading_Leveraged_Equity", "MS_Trading_Miscellaneous", "Trading_Miscellaneous", "MS_Volatility", "Volatility", "MS_Commodities_Broad_Basket", "Commodities_Broad_Basket",
      "MS_Commodities_Precious_Met", "Commodities_Precious_Met", "MS_Convertibles", "Convertibles", "MS_China_Region", "China_Region", "MS_Communications", "Communications",
      "MS_Consumer_Cyclical", "Consumer_Cyclical", "MS_Consumer_Defensive", "Consumer_Defensive", "MS_Diversified_Pacific_Asia", "Diversified_Pacific_Asia", "MS_Energy_Limited_Partnersh",
      "Energy_Limited_Partnersh", "MS_Equity_Energy", "Equity_Energy", "MS_Equity_Precious_Metals", "Equity_Precious_Metals", "MS_Financial", "Financial", "MS_Foreign_Large_Value", "Foreign_Large_Value",
      "MS_Foreign_Small_Mid_Growth", "Foreign_Small_Mid_Growth", "MS_Foreign_Small_Mid_Value", "Foreign_Small_Mid_Value", "MS_investments", "investments", "MS_India_Equity", "India_Equity",
      "MS_Industrials", "Industrials", "MS_Japan_Stock", "Japan_Stock", "MS_Large_Blend", "Large_Blend", "MS_Latin_America_Stock", "Latin_America_Stock", "MS_Mid_Cap_Value", "Mid_Cap_Value",
      "MS-Miscellaneous_Region", "Miscellaneous_Region", "MS_Miscellaneous_Sector", "Miscellaneous_Sector", "MS_Natural_Resources", "Natural_Resources", "MS_Small_Blend", "Small_Blend",
      "MS_Technology", "Technology", "MS_Utilities", "Utilities", "MS_Bank_Loan", "Bank_Loan", "MS_Inflation_Protected_Bond", "Inflation_Protected_Bond", "MS_Long_Government", "Long_Government",
      "MS_Long_Term_Bond", "Long_Term_Bond", "MS_Multisector_Bond", "Multisector_Bond", "MS_Preferred_Stock", "Preferred_Stock", "MS_Ultrashort_Bond", "Ultrashort_Bond", "MS_High_Yield_Muni",
      "High_Yield_Muni", "MS_Muni_California_Intermed", "Muni_California_Intermed", "MS_Muni_California_Long", "Muni_California_Long", "MS_Muni_Massachusetts", "Muni_Massachusetts",
      "MS_Muni_Minnesota", "Muni_Minnesota", "MS_Muni_National_Interm", "Muni_National_Interm", "MS_Muni_National_Short", "Muni_National_Short", "MS_Muni_New_Jersey", "Muni_New_Jersey",
      "MS_Muni_New_York_Intermedia", "Muni_New_York_Intermedia", "MS_Muni_New_York_Long", "Muni_New_York_Long", "MS_Muni_Ohio", "Muni_Ohio", "MS_Muni_Pennsylvania", "Muni_Pennsylvania",
      "MS_Muni_Single_State_Interm", "Muni_Single_State_Interm", "MS_Muni_Single_State_Long", "Muni_Single_State_Long", "MS_Muni_Single_State_Short", "Muni_Single_State_Short" ]
        result_list=[]
        for tuple in list1[:-1:2]:
            idx = list1.index(tuple)
            list_temp = [list1[idx], list2[idx+13], list1[idx+1], list2[idx+14]]
            result_list.append(list_temp)
        return result_list


    new_tuple = [ "Steward Norman", "07 Golden Leaf Street", "21220", "Milford", "", "CT", "W09", "261881.07", "6259581.19", "29452.1", "589042", "0", "282959", "257.2122", "4286.87", "0", "89071.85", "0", "13172.35", "121.9982", "6099.91", "257.2122", "4286.87", "555.5656", "6944.57", "1263.8755", "25277.51", "1909.9913", "27285.59", "1163.8326", "19397.21", "524.8782", "7498.26", "0", "47154.48", "988.1874", "16469.79", "3171.0602", "45300.86", "6496.6264", "81207.83", "0", "50789.96", "13640.9792", "341024.48", "1767.0422", "25243.46", "1211.0529", "40368.43", "3387.5975", "48394.25", "0", "74047.86", "0", "28590.26", "1408.477", "20121.1", "1226.2798", "61313.99", "4082.3916", "58319.88", "5247.8392", "65597.99", "4652.6244", "77543.74", "599.1748", "8559.64", "2118.6978", "5311.63", "3261.3256", "40766.57", "0", "48394.25", "3702.393", "74047.86", "1143.6104", "28590.26", "1006.055", "20121.1", "3678.8394", "61313.99", "2332.7952", "58319.88", "1967.9397", "65597.99", "4652.6244", "77543.74", "427.982", "8559.64", "1412.4652", "35311.63", "2445.9942", "40766.57", "3877.187", "77543.74", "513.5784", "8559.64", "2471.8141", "35311.63", "2038.3285", "40766.57", "4665.5904", "58319.88", "3279.8995", "65597.99", "3877.187", "77543.74", "427.982", "8559.64", "706.2326", "5311.63", "815.3314", "40766.57", "2903.655", "48394.25", "\t3702.393", "74047.86", "1143.6104", "28590.26", "804.844", "20121.1", "2452.5596", "61313.99", "2332.7952", "58319.88", "2623.9196", "65597.99", "2326.3122", "77543.74", "2332.7952", "\t58319.88", "1967.9397", "65597.99", "3101.7496", "77543.74", "513.5784", "8559.64", "706.2326", "35311.63", "2038.3285", "40766.57", "2419.7125", "48394.25", "3702.393", "74047.86", "1429.513", "28590.26", "1006.055", "20121.1", "3678.8394", "61313.99", "2915.994", "58319.88", "1311.9598", "65597.99", "6978.9366", "77543.74", "5923.8288", "74047.86", "1429.513", "28590.26", "1207.266", "20121.1", "3065.6995", "61313.99", "1749.5964", "58319.88", "2623.9196", "65597.99", "2326.3122", "77543.74", "3702.393", "74047.86", "1715.4156", "28590.26", "1207.266", "20121.1", "3678.8394", "61313.99", "2915.994", "58319.88", "1311.9598", "65597.99", "4652.6244", "77543.74", "2961.9144", "74047.86", "1143.6104", "28590.26", "402.422", "20121.1", "4291.9793", "\t61313.99", "2332.7952", "58319.88", "3279.8995", "65597.99", "3101.7496", "77543.74", "5923.8288", "74047.86", "1429.513", "28590.26", "804.844", "20121.1", "1839.4197", "61313.99", "\t1166.3976", "58319.88", "1967.9397", "65597.99", "2326.3122", "77543.74", "2961.9144", "74047.86", "1429.513", "28590.26", "402.422", "20121.1" ]
    result = process(new_tuple)
    print result
