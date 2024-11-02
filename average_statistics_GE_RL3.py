import os
import pandas as pd
import numpy as np
import glob

# csv_list = glob.glob('2020-no-buffer-eval/*.csv')

# p_list = []
# r_list = []
# f_list = []
# for c in csv_list:
#     df = pd.read_csv(c)
#     p_list.append(df.at[0,'pre'])
#     r_list.append(df.at[0,'rec'])
#     f_list.append(df.at[0,'f1s'])

# print(np.mean(p_list), np.mean(r_list), np.mean(f_list))

def main():
    pd_final = pd.DataFrame({})
    for county in ['130634', '411523', '610426','130631','130636', '130529', '341203', '130532', '130531', '130434']:
    # ['130634', '411523', '610426','130631', '469001', '130636', '130529', '341203', '130532', '130531', '130434', '130924' , '469024', '130925', '360781']:
    # ['130434', '411523', '130530', '130631', '469001', '130636', '130529', '341203', '130532', '130531', '130434', '620102', '469024', '130925', '360781', '610426', '130924', '131124', '620802', '130425', '130533', '131128', '411625', '130125', '520328', '130522', '140829', '410328', '341322', '130927', '610826', '451022', '610430']:
    # ['500241', '610329', '141034', '341203', '360724', '360781', '522635', '341523', '130636', '360830', '520328', '520327', '610826', '450123', '411324', '130425', '430822', '411625', '130925', '610426', '532324', '130434', '540229', '411523', '360321', '130924', '530827', '410327', '522327', '130522', '622901', '431228', '530829', '630203', '431028', '621125', '430821', '131123', '130125', '513437', '620523', '610929', '433123', '410927', '140723', '140931', '130708', '140427', '130927', '622923', '522326', '610926', '141126', '130727', '451022', '131128', '610430', '469024', '130529', '532325', '620102', '360821', '530624', '520424', '469030', '610222', '410225', '530923', '513322', '533301', '620802', '410328', '610729', '431225', '430225', '341322', '130731', '130533', '130126', '520326', '340828', '511529', '522729', '140927', '522632', '360726', '510824', '451121', '433130', '530521', '140223', '522325', '130630', '530629', '610727', '620821', '511602', '450329', '140929', '610831', '532925', '540502', '520624', '630225', '130531', '469001', '610328', '140224', '530924', '520425', '532932', '610527', '511381', '620525', '140221', '522623', '513435', '420529', '140429', '141030', '431027', '131124', '520324', '340826', '431230', '130624', '140928', '422827', '532523', '131122', '620122', '450125', '411422', '532931', '520403', '130129', '410325', '130631', '520525', '520203', '130728', '430529', '340827', '610924', '533122', '141028', '522634', '411723', '140829', '451027', '130530', '361125', '610722', '141127', '360828', '422823', '640402', '532601', '130709', '522628', '610927', '141129', '540104', '411321', '520628', '513338', '140215', '140425', '510525', '540123', '130532', '130634']:

    # ['131128','130925','141034','131123','130631','130531','130532','130529','130533','610328','130522']:
        if not os.path.exists('../output2_GE_directly_add_RL3/'+county+'_0.01_test.csv'): #'2023_eval_buffer_GT/'+
            continue
        pd_tmp = pd.read_csv('../output2_GE_directly_add_RL3/'+county+'_0.01_test.csv')
        pd_final = pd.concat([pd_final,pd_tmp])

    pd_final.to_csv('../output2_GE_directly_add_RL3/road_eval_2020_statistics.csv', index=False)
    print(np.average(list(pd_final['pre'])))
    print(np.average(list(pd_final['rec'])))
    print(np.average(list(pd_final['f1s'])))


    # pd_final = pd.DataFrame({})
    # for county in ['130634', '411523', '610426','130631', '469001', '130636', '130529', '341203', '130532', '130531', '130434', '130924' , '469024', '130925', '360781']:
    # # ['130634', '411523', '130530', '130631', '469001', '130636', '130529', '341203', '130532', '130531', '130434', '620102', '469024', '130925', '360781', '610426', '130924', '131124', '620802', '130425', '130533', '131128', '411625', '130125', '520328', '130522', '140829', '410328', '341322', '130927', '610826', '451022', '610430']:
    # # ['500241', '610329', '141034', '341203', '360724', '360781', '522635', '341523', '130636', '360830', '520328', '520327', '610826', '450123', '411324', '130425', '430822', '411625', '130925', '610426', '532324', '130434', '540229', '411523', '360321', '130924', '530827', '410327', '522327', '130522', '622901', '431228', '530829', '630203', '431028', '621125', '430821', '131123', '130125', '513437', '620523', '610929', '433123', '410927', '140723', '140931', '130708', '140427', '130927', '622923', '522326', '610926', '141126', '130727', '451022', '131128', '610430', '469024', '130529', '532325', '620102', '360821', '530624', '520424', '469030', '610222', '410225', '530923', '513322', '533301', '620802', '410328', '610729', '431225', '430225', '341322', '130731', '130533', '130126', '520326', '340828', '511529', '522729', '140927', '522632', '360726', '510824', '451121', '433130', '530521', '140223', '522325', '130630', '530629', '610727', '620821', '511602', '450329', '140929', '610831', '532925', '540502', '520624', '630225', '130531', '469001', '610328', '140224', '530924', '520425', '532932', '610527', '511381', '620525', '140221', '522623', '513435', '420529', '140429', '141030', '431027', '131124', '520324', '340826', '431230', '130624', '140928', '422827', '532523', '131122', '620122', '450125', '411422', '532931', '520403', '130129', '410325', '130631', '520525', '520203', '130728', '430529', '340827', '610924', '533122', '141028', '522634', '411723', '140829', '451027', '130530', '361125', '610722', '141127', '360828', '422823', '640402', '532601', '130709', '522628', '610927', '141129', '540104', '411321', '520628', '513338', '140215', '140425', '510525', '540123', '130532', '130634']:

    # # ['131128','130925','141034','131123','130631','130531','130532','130529','130533','610328','130522']:
    #     if not os.path.exists('../output2/'+county+'_0.001_test.csv'): #'2023_eval_buffer_GT/'+
    #         continue
    #     pd_tmp = pd.read_csv('../output2/'+county+'_0.001_test.csv')
    #     pd_final = pd.concat([pd_final,pd_tmp])

    # pd_final.to_csv('../output2/road_eval_2020_statistics_0001.csv', index=False)
    # print(np.average(list(pd_final['pre'])))
    # print(np.average(list(pd_final['rec'])))
    # print(np.average(list(pd_final['f1s'])))

if __name__ == "__main__":
    main()