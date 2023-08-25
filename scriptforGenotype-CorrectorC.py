#PBS -N geno_corrector
#PBS -l nodes=1:ppn=8,vmem=16gb,walltime=250:00:00
#PBS -q default

cd $PBS_O_WORKDIR

module load Genotype-corrector/1.0


python -m schnablelab.imputation.GC qc_sd ABH40formattoGC0.03.map F2PEPPER400.03qc_sd.map --population F2

python -m schnablelab.imputation.GC qc_hetero F2PEPPER400.03qc_sd.map F2PEPPER400.03qc_hetero.map

python -m schnablelab.imputation.GC correct config.txt F2PEPPER400.03qc_hetero.map --debug

python -m schnablelab.imputation.GC cleanup F2PEPPER400.03qc_hetero.corrected.map.debug F2PEPPER400.03_modifed.map

python -m schnablelab.imputation.GC bin F2PEPPER400.03qc_hetero.corrected.map F2PEPPERsuper400.03_final.map

python -m schnablelab.imputation.GC format F2PEPPERsuper400.03_final.map --rqtl --pop_type F2



