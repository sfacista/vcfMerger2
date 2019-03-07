## methods to filter the vcf reords already brought up to specs using by current tool or performed by user


def filtering_ala_tgen(v, column_tumor = 11 , column_normal = 10):
	'''
	Variants Filtering criteria defined by TGen company
	The Filtering is specific for Somatic Variants only and work also only and only if there are only 2 samples
	defined in the column 10 and 11 of the vcf file.
	Expect Normal sample in column 10
	Expect Tumor sample in column 11

	:param v: object Variant from cyvcf2 class
	:return: v if PASS all filtering or None if at least one filter FAILS

	'''
	## definition of threshold variables, with threshold specific to tgen definition
	th_tumor_AR = 0.05 ##  Mutation should be at least 5% or above in  the Tumor Sample
	th_normal_AR = 0.02  ##  Mutation should be less than 2% normal Sample
	th_tumor_DP = 10  ##  Mutation should be covered by at least 10 reads in the Tumor Sample
	th_normal_DP = 10  ##  Mutation should be covered by at least 10 reads in the Normal Sample

	## need to know the column number to be sure that we filter on the correct sample
	## default should be: col_tumor = 11 ; col_normal = 10 or vice-versa ;
	idxT = 1 if column_tumor == 11 else 0
	idxN = 0 if column_normal == 10 else 1
	if v.format('AR')[idxT] >= th_tumor_AR \
			and v.format('AR')[idxN] <= th_normal_AR \
			and v.format('DP')[idxT] >= th_tumor_DP \
			and v.format('DP')[idxN] >= th_normal_DP:
		return v
	else:
		return None



def filter_using_file_template(v, ff):
	"""

	:param ff:
	:return: v
	"""
	pass