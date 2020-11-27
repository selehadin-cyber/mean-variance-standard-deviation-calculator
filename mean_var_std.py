import numpy as np

def calculate(list):
  a = np.array(list)
  a.resize(3, 3)
  print(a)
  flattenedmean = np.mean(a)
  flattenedvariance = np.var(a)
  flattenedstandardD = np.std(a)
  axis1mean = np.mean(a, axis=0)
  axis2mean = np.mean(a, axis=1)
  axis1variance = np.var(a, axis=0)
  axis2variance = np.var(a, axis=1)
  axis1std = np.var(a, axis=0)
  axis2std = np.var(a, axis=1)
  flattenedmax = np.max(a)
  axis1max = np.max(a, axis=0)
  axis2max = np.max(a, axis=1)
  flattenedmin = np.min(a)
  axis1min = np.min(a, axis=0)
  axis2min = np.min(a, axis=1)
  flattenedsum = np.sum(a)
  axis1sum = np.sum(a, axis=0)
  axis2sum = np.sum(a, axis=1)
  calculations = {
  'mean': [axis1mean.tolist(), axis2mean.tolist(), flattenedmean],
  'variance': [axis1variance.tolist(), axis2variance.tolist(), flattenedvariance],
  'standard deviation': [axis1std.tolist(), axis2std.tolist(), flattenedstandardD],
  'max': [axis1max.tolist(), axis2max.tolist(), flattenedmax],
  'min': [axis1min.tolist(), axis2min.tolist(), flattenedmin],
  'sum': [axis1sum.tolist(), axis2sum.tolist(), flattenedsum]
}


  return calculations