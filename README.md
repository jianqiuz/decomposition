# decomposition
This anaerobic carbon decomposition model is implemented in PHREEQC (V3.0)

Citation: Zheng, J., Thornton, P. E., Painter, S. L., Gu, B., Wullschleger, S. D., and Graham, D. E.: Modeling anaerobic soil organic carbon decomposition in Arctic polygon tundra: insights into soil geochemical influences on carbon mineralization, Biogeosciences Discuss., https://doi.org/10.5194/bg-2018-63, in review, 2018.

Step 1: PHREEQC installation (Mac system)
Download is available on USGS website https://wwwbrr.cr.usgs.gov/projects/GWC_coupled/phreeqc/

In the .bash_profile under the home directory:  
export PATH="/Users/Jianqiu/Applications/phreeqc/bin:$PATH"
export PHREEQC_DATABASE=/Users/Jianqiu/Applications/phreeqc/database/phreeqc.dat

Step 2: Database development
The database developed in this paper (redox.dat) included simplified CLM-CN carbon decomposition cascade, fermentation, methanogenesis, iron reduction, and WHAM pH buffering model. In order to run PHREEQC using redox.dat, simply copy and paste the .dat file under the database directory

Step 3: Run the python script to generate PHREEQC executable .phrq files. 
File LCP_C1O_4.phrq is a sample PHREEQC input file and lcp_c1o_4.txt is the corresponding output file.
