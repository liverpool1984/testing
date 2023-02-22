strin = '22 Feb 12:40:52 1 сек! рост по dogeusdt на prcnt_pre=7.24 max_price=0.09076 min_pre=0.08463 max_pre_pre=0.08555 prcnt_pre_pre=6.09 last_5_prcnt=[1.079, 0.857, 0.762, 2.578, 2.191, 2.956] last_5_from_max=[2.975, 2.292, 1.697, 0.0, 0.408, 0.474]'


srr = strin.split()
result = [srr[0] + ' ' + srr[1] + ' ' + srr[2],
          srr[7],
          float(srr[9].split('=')[-1]),
          srr[14].split('[')[-1][:-1],
          srr[15][:-1],
          srr[16][:-1],
          srr[17][:-1],
          srr[18][:-1],
          srr[19][:-1],
          srr[20].split('[')[-1][:-1],
          srr[21][:-1],
          srr[22][:-1],
          srr[23][:-1],
          srr[24][:-1],
          srr[25][:-1],
          ]

print(result)
