
def fileChecker(data, context):
    resources = ['01CIP2_G01', '01T_ASIA_G01', '01S_ENRO_G01', '03INGRID_GS1', '03INGRID_GS2', '03INGRID_GS3', '03INGRID_GS4', '03INGRID_GS5', '03INGRID_GS6', '03ALMNOS_BAT1', '03ALMNOS_BAT2']
    
    filename = 'DCSResourceCompliance_DTC_01CAPRIS_G01_20210927_1140_4355.csv'
    resource = filename.split('_')

    if (resource[2] in resources):
        print('sheesh')
