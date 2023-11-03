#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-seriation
Version  : 1.5.1
Release  : 70
URL      : https://cran.r-project.org/src/contrib/seriation_1.5.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/seriation_1.5.1.tar.gz
Summary  : Infrastructure for Ordering Objects Using Seriation
Group    : Development/Tools
License  : GPL-3.0
Requires: R-seriation-lib = %{version}-%{release}
Requires: R-TSP
Requires: R-ca
Requires: R-colorspace
Requires: R-foreach
Requires: R-gclus
Requires: R-qap
Requires: R-registry
Requires: R-vegan
BuildRequires : R-TSP
BuildRequires : R-ca
BuildRequires : R-colorspace
BuildRequires : R-dendextend
BuildRequires : R-foreach
BuildRequires : R-gclus
BuildRequires : R-qap
BuildRequires : R-registry
BuildRequires : R-vegan
BuildRequires : buildreq-R

%description
seriation/sequencing/ordination techniques to reorder matrices, dissimilarity
    matrices, and dendrograms. Also provides (optimally) reordered heatmaps,
    color images and clustering visualizations like dissimilarity plots, and

%package lib
Summary: lib components for the R-seriation package.
Group: Libraries

%description lib
lib components for the R-seriation package.


%prep
%setup -q -n seriation
pushd ..
cp -a seriation buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689954649

%install
export SOURCE_DATE_EPOCH=1689954649
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/seriation/README_files/configuration-1.png
/usr/lib64/R/library/seriation/README_files/seriation-1.png
/usr/lib64/R/library/seriation/README_files/seriation-2.png
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
/usr/lib64/R/library/seriation/help/figures/logo.svg
/usr/lib64/R/library/seriation/help/paths.rds
/usr/lib64/R/library/seriation/help/seriation.rdb
/usr/lib64/R/library/seriation/help/seriation.rdx
/usr/lib64/R/library/seriation/html/00Index.html
/usr/lib64/R/library/seriation/html/R.css
/usr/lib64/R/library/seriation/tests/testthat.R
/usr/lib64/R/library/seriation/tests/testthat/test-criterion.R
/usr/lib64/R/library/seriation/tests/testthat/test-dissimilarity.R
/usr/lib64/R/library/seriation/tests/testthat/test-map.R
/usr/lib64/R/library/seriation/tests/testthat/test-permuation_vector.R
/usr/lib64/R/library/seriation/tests/testthat/test-seriate.R
/usr/lib64/R/library/seriation/tests/testthat/test-zzz_seriate_extra.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/seriation/libs/seriation.so
/usr/lib64/R/library/seriation/libs/seriation.so.avx2
/usr/lib64/R/library/seriation/libs/seriation.so.avx512
