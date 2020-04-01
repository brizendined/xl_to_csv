# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:10:44 2020

@author: d_bri
"""



def make_csv(infile,outfile):
        
    import pandas as pd
    import csv
    from datetime import datetime
    
    #output_file='csv_out.csv'
    
    try:
        data=pd.read_excel(infile)
        #print('pandas DataFrame')
        #print(data)
        #print(type(data))
        
        data_list=data.values.tolist()
        final_list=[]
        
        #scrub commas
        for row in data_list:
            new_row=[]
            for col in row:
                #print(col,type(col))
                if type(col) is str:
                    e=col.replace(',','')
                elif pd.isnull(col):
                    e=''
                elif isinstance(col, datetime):
                    e=col.strftime('%m/%d/%Y %H:%M:%S')
                else:
                    e=col
                    
                new_row.append(e)
    
            final_list.append(new_row)
        
        try:
            with open(outfile,'w') as output:
                writer=csv.writer(output, lineterminator='\n')
                writer.writerows(final_list)
                
            return 1
        except:
            return 0
        
    except FileNotFoundError:
        return 0
