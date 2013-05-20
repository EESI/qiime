#!/usr/bin/env python
# File created on 02 May 2013
from __future__ import division


"""
	This is a test unit for the Fizzy feature selection algorithm, which uses
	the PyFeast python module. If the unit test fails, then it is likely that 
	you do not have PyFeast installed on the system. 

	After PyFeast is installed you should be good to go. If you have any 
	questions feel free to email gregory.ditzler@gmail.com 
"""


__author__ = "Gregory Ditzler"
__copyright__ = "Copyright 2011, The QIIME project"
__credits__ = ["Gregory Ditzler", "Calvin Morrison", "Gail Rosen"]
__license__ = "GPL"
__version__ = "1.7.0-dev"
__maintainer__ = "Gregory Ditzler"
__email__ = "gregory.ditzler@gmail.com"
__status__ = "Development"

import qiime.fizzy as fizzy 

def main():
	"""
		main()
		No input agruments

		Run the fizzy module with data that is in qiime/tests/test_fizzy/
		directory. The result should be in output.txt. If the file is not
		there then there was likely an error. 
	"""
	data_file = open('./test_fizzy/data.biom','U')
	label_file = open('./test_fizzy/labels.map','U')
	n_select = 25
	method = 'mim'
	col_name = 'Class'
	outfile = './test_fizzy/output.txt'
	try:
		# if this throws an error then it is likely that PyFeast has not
		# been installed. 
		fizzy.run_feature_selection(data_file, label_file, col_name, outfile, method, n_select)
		print 'Refer to the test_fizzy directory for output.txt '
		f = open('./test_fizzy/output.txt','U')
		print f.read()
		f.close()
	except ValueError:
		print 'Something is broken in Fizzy! Do you have PyFeast installed?'

	return None


if __name__ == "__main__":
	main()
