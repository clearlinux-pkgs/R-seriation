#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-seriation
Version  : 1.2.3
Release  : 18
URL      : https://cran.r-project.org/src/contrib/seriation_1.2-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/seriation_1.2-3.tar.gz
Summary  : Infrastructure for Ordering Objects Using Seriation
Group    : Development/Tools
License  : GPL-3.0
Requires: R-seriation-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-gridExtra
Requires: R-pillar
Requires: R-pkgconfig
Requires: R-rlang
Requires: R-viridisLite
BuildRequires : R-DEoptimR
BuildRequires : R-Rcpp
BuildRequires : R-TSP
BuildRequires : R-caTools
BuildRequires : R-colorspace
BuildRequires : R-dendextend
BuildRequires : R-diptest
BuildRequires : R-fpc
BuildRequires : R-gclus
BuildRequires : R-gdata
BuildRequires : R-ggplot2
BuildRequires : R-gplots
BuildRequires : R-gridExtra
BuildRequires : R-gtable
BuildRequires : R-gtools
BuildRequires : R-lazyeval
BuildRequires : R-modeltools
BuildRequires : R-munsell
BuildRequires : R-pillar
BuildRequires : R-pkgconfig
BuildRequires : R-plyr
BuildRequires : R-qap
BuildRequires : R-registry
BuildRequires : R-rlang
BuildRequires : R-scales
BuildRequires : R-tibble
BuildRequires : R-viridis
BuildRequires : R-viridisLite
BuildRequires : R-whisker
BuildRequires : buildreq-R

%description
# seriation - Infrastructure for Ordering Objects Using Seriation - R package
[![CRAN version](http://www.r-pkg.org/badges/version/seriation)](https://cran.r-project.org/package=seriation)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/seriation)](https://cran.r-project.org/package=seriation)
[![Travis-CI Build Status](https://travis-ci.org/mhahsler/seriation.svg?branch=master)](https://travis-ci.org/mhahsler/seriation)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/mhahsler/seriation?branch=master&svg=true)](https://ci.appveyor.com/project/mhahsler/seriation)

%package lib
Summary: lib components for the R-seriation package.
Group: Libraries

%description lib
lib components for the R-seriation package.


%prep
%setup -q -c -n seriation

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552944306

%install
export SOURCE_DATE_EPOCH=1552944306
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library seriation
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library seriation
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library seriation
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  seriation || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/seriation/CITATION
/usr/lib64/R/library/seriation/DESCRIPTION
/usr/lib64/R/library/seriation/INDEX
/usr/lib64/R/library/seriation/Meta/Rd.rds
/usr/lib64/R/library/seriation/Meta/data.rds
/usr/lib64/R/library/seriation/Meta/features.rds
/usr/lib64/R/library/seriation/Meta/hsearch.rds
/usr/lib64/R/library/seriation/Meta/links.rds
/usr/lib64/R/library/seriation/Meta/nsInfo.rds
/usr/lib64/R/library/seriation/Meta/package.rds
/usr/lib64/R/library/seriation/Meta/vignette.rds
/usr/lib64/R/library/seriation/NAMESPACE
/usr/lib64/R/library/seriation/NEWS.md
/usr/lib64/R/library/seriation/R/seriation
/usr/lib64/R/library/seriation/R/seriation.rdb
/usr/lib64/R/library/seriation/R/seriation.rdx
/usr/lib64/R/library/seriation/data/Chameleon.rda
/usr/lib64/R/library/seriation/data/Irish.rda
/usr/lib64/R/library/seriation/data/Munsingen.rda
/usr/lib64/R/library/seriation/data/Psych24.rda
/usr/lib64/R/library/seriation/data/SupremeCourt.rda
/usr/lib64/R/library/seriation/data/Townships.rda
/usr/lib64/R/library/seriation/data/Wood.rda
/usr/lib64/R/library/seriation/data/Zoo.rda
/usr/lib64/R/library/seriation/doc/index.html
/usr/lib64/R/library/seriation/doc/seriation.R
/usr/lib64/R/library/seriation/doc/seriation.Rnw
/usr/lib64/R/library/seriation/doc/seriation.pdf
/usr/lib64/R/library/seriation/help/AnIndex
/usr/lib64/R/library/seriation/help/aliases.rds
/usr/lib64/R/library/seriation/help/paths.rds
/usr/lib64/R/library/seriation/help/seriation.rdb
/usr/lib64/R/library/seriation/help/seriation.rdx
/usr/lib64/R/library/seriation/html/00Index.html
/usr/lib64/R/library/seriation/html/R.css
/usr/lib64/R/library/seriation/tests/testthat.R
/usr/lib64/R/library/seriation/tests/testthat/test-DendSer_GA.R
/usr/lib64/R/library/seriation/tests/testthat/test-criterion.R
/usr/lib64/R/library/seriation/tests/testthat/test-dissimilarity.R
/usr/lib64/R/library/seriation/tests/testthat/test-permuation_vector.R
/usr/lib64/R/library/seriation/tests/testthat/test-seriate.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/seriation/libs/seriation.so
/usr/lib64/R/library/seriation/libs/seriation.so.avx2
/usr/lib64/R/library/seriation/libs/seriation.so.avx512
