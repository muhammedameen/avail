def tree(LOAN, MORTDUE, REASON, VALUE, DELINQ, DEROG, CLAGE, Other, DELINQ, Office, Sales, ProfExe):
  if DELINQ <= 0.9998865127563477:
    if CLAGE <= 178.02609252929688:
      if DEROG <= 0.674604594707489:
        if LOAN <= 5750.0:
          return [[ 41. 161.]]
        else:  # if LOAN > 5750.0
          if Office <= 0.03917144611477852:
            if LOAN <= 17050.0:
              if MORTDUE <= 67090.0:
                if LOAN <= 11050.0:
                  return [[102. 229.]]
                else:  # if LOAN > 11050.0
                  return [[153. 179.]]
              else:  # if MORTDUE > 67090.0
                return [[217. 130.]]
            else:  # if LOAN > 17050.0
              if MORTDUE <= 48493.5:
                return [[179.  52.]]
              else:  # if MORTDUE > 48493.5
                return [[268. 171.]]
          else:  # if Office > 0.03917144611477852
            return [[357. 106.]]
      else:  # if DEROG > 0.674604594707489
        return [[ 95. 315.]]
    else:  # if CLAGE > 178.02609252929688
      if DEROG <= 0.4712521433830261:
        if Office <= 0.6086692214012146:
          if LOAN <= 24750.0:
            if VALUE <= 81550.0:
              return [[291.  95.]]
            else:  # if VALUE > 81550.0
              if MORTDUE <= 73095.0:
                return [[196.  11.]]
              else:  # if MORTDUE > 73095.0
                return [[284.  81.]]
          else:  # if LOAN > 24750.0
            return [[246. 105.]]
        else:  # if Office > 0.6086692214012146
          return [[201.  19.]]
      else:  # if DEROG > 0.4712521433830261
        return [[116.  86.]]
  else:  # if DELINQ > 0.9998865127563477
    if DEROG <= 0.7394163012504578:
      if DELINQ <= 1.6083570718765259:
        if CLAGE <= 202.7852325439453:
          return [[157. 310.]]
        else:  # if CLAGE > 202.7852325439453
          return [[121.  79.]]
      else:  # if DELINQ > 1.6083570718765259
        if DELINQ <= 3.5:
          return [[104. 291.]]
        else:  # if DELINQ > 3.5
          return [[ 26. 196.]]
    else:  # if DEROG > 0.7394163012504578
      if DELINQ <= 2.5:
        return [[ 52. 329.]]
      else:  # if DELINQ > 2.5
        return [[  8. 224.]]