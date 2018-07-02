#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pbivnorm
Version  : 0.6.0
Release  : 4
URL      : https://cran.r-project.org/src/contrib/pbivnorm_0.6.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pbivnorm_0.6.0.tar.gz
Summary  : Vectorized Bivariate Normal CDF
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-pbivnorm-lib
BuildRequires : clr-R-helpers

%description
probabilities from a standard bivariate normal CDF.

%package lib
Summary: lib components for the R-pbivnorm package.
Group: Libraries

%description lib
lib components for the R-pbivnorm package.


%prep
%setup -q -c -n pbivnorm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530315611

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530315611
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbivnorm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbivnorm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbivnorm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library pbivnorm|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pbivnorm/DESCRIPTION
/usr/lib64/R/library/pbivnorm/INDEX
/usr/lib64/R/library/pbivnorm/Meta/Rd.rds
/usr/lib64/R/library/pbivnorm/Meta/features.rds
/usr/lib64/R/library/pbivnorm/Meta/hsearch.rds
/usr/lib64/R/library/pbivnorm/Meta/links.rds
/usr/lib64/R/library/pbivnorm/Meta/nsInfo.rds
/usr/lib64/R/library/pbivnorm/Meta/package.rds
/usr/lib64/R/library/pbivnorm/NAMESPACE
/usr/lib64/R/library/pbivnorm/NEWS
/usr/lib64/R/library/pbivnorm/R/pbivnorm
/usr/lib64/R/library/pbivnorm/R/pbivnorm.rdb
/usr/lib64/R/library/pbivnorm/R/pbivnorm.rdx
/usr/lib64/R/library/pbivnorm/help/AnIndex
/usr/lib64/R/library/pbivnorm/help/aliases.rds
/usr/lib64/R/library/pbivnorm/help/paths.rds
/usr/lib64/R/library/pbivnorm/help/pbivnorm.rdb
/usr/lib64/R/library/pbivnorm/help/pbivnorm.rdx
/usr/lib64/R/library/pbivnorm/html/00Index.html
/usr/lib64/R/library/pbivnorm/html/R.css
/usr/lib64/R/library/pbivnorm/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/pbivnorm/libs/pbivnorm.so
/usr/lib64/R/library/pbivnorm/libs/pbivnorm.so.avx2
/usr/lib64/R/library/pbivnorm/libs/pbivnorm.so.avx512
