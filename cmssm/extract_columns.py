"""
Creates hdf5 file with only the specified columns from the full dataset.
This is useful space saving measure as while the full dataset is quite large
only a few columns are of interest.
"""
import h5py
import numpy as np

def main():
    columns = [
        '#CMSSM_parameters @CMSSM::primary_parameters::A0',
        '#CMSSM_parameters @CMSSM::primary_parameters::M0',
        '#CMSSM_parameters @CMSSM::primary_parameters::M12',
        '#CMSSM_parameters @CMSSM::primary_parameters::SignMu',
        '#CMSSM_parameters @CMSSM::primary_parameters::TanBeta',
        '#LHC_Combined_LogLike @ColliderBit::calc_LHC_LogLike'
    ]
    extract('CMSSM.hdf5', 'CMSSM_subset.hdf5', 'CMSSM', columns)


def extract(src_path, dst_path, group, columns):
    src_fd = h5py.File(src_path, 'r')
    src = src_fd[group]
    dst = h5py.File(dst_path, 'w')

    srcsize = src[columns[0]].shape[0]
    chunksize = src[columns[0]].chunks[0]

    # We need to filter out points that are invalid in some way. We do this by
    # checking that the point is valid in all columns. If it is; then keep it,
    # otherwise throw it out. GAMBIT store the validity of the points in a
    # separate column named <column_name>_isvalid.
    isvalid = np.ones(src[columns[0]].shape, dtype=np.bool)
    for c in ['%s_isvalid' % i for i in columns]:
        for i in range(0, srcsize, chunksize):
            isvalid[i:i+chunksize] = np.logical_and(isvalid[i:i+chunksize],
                                                    src[c][i:i+chunksize])

    dstsize = np.sum(isvalid)
    print('Keeping %i valid points out of %i total.' % (dstsize, srcsize))

    for c in columns:
        print(c)
        dst.create_dataset(c,
                           shape=(dstsize,),
                           maxshape=(None,),
                           dtype=np.float64,
                           chunks=(chunksize,),
                           compression='lzf',
                           shuffle=True)

        j = 0 # need separate indices as we do only copy over valid points.
        for i in range(0, srcsize, chunksize):
            nvalid = np.sum(isvalid[i:i+chunksize])
            dst[c][j:j+nvalid] = src[c][i:i+chunksize][isvalid[i:i+chunksize]]
            j += nvalid

    src_fd.close()
    dst.close()


if __name__ == '__main__':
    main()
