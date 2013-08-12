%define	modname	Compress-Raw-Bzip2
%define	modver	2.062

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	1

Summary:	Low-Level Interface to bzip2 compression library
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{modname}-%{modver}.tar.gz

BuildRequires:	bzip2-devel
BuildRequires:	perl-devel

%description
Low-Level Interface to bzip2 compression library.

%prep
%setup -q -n %{modname}-%{modver}

%build
BUILD_BZIP2=0 perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/Compress
%{perl_vendorarch}/auto/Compress
%{_mandir}/man3/Compress::Raw::Bzip2.3pm*

%changelog
* Sat Dec 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.59.0-1
- build against system libbz2
- cleanups
- new version

* Tue Mar 13 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.49.0-1
+ Revision: 784850
- new version
- clean out spec

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.37.0-4
+ Revision: 765100
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.37.0-3
+ Revision: 763561
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 2.37.0-2
+ Revision: 763292
- force it

* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.37.0-1
+ Revision: 686969
- update to new version 2.037

* Sun May 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.35.0-1
+ Revision: 672606
- update to new version 2.035

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.33.0-3
+ Revision: 667050
- mass rebuild

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 2.33.0-2
+ Revision: 640742
- rebuild to obsolete old packages

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.33.0-1
+ Revision: 634214
- update to new version 2.033

* Wed Jan 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.32.0-3
+ Revision: 633007
- don't remove the man page, the conflict has been fixed

* Mon Jan 24 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.32.0-2
+ Revision: 632463
- fix file conflicts on docs

* Fri Jan 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 629478
- update to new version 2.032

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.31.0-1mdv2011.0
+ Revision: 595085
- update to new version 2.031

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-2mdv2011.0
+ Revision: 562439
- rebuild

* Sun Jul 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.30.0-1mdv2011.0
+ Revision: 559337
- update to new version 2.030

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.27.0-2mdv2011.0
+ Revision: 555698
- rebuild

* Mon Apr 26 2010 Jérôme Quelin <jquelin@mandriva.org> 2.27.0-1mdv2010.1
+ Revision: 539067
- update to 2.027

* Thu Apr 08 2010 Jérôme Quelin <jquelin@mandriva.org> 2.26.0-1mdv2010.1
+ Revision: 533042
- update to 2.026

* Mon Mar 29 2010 Jérôme Quelin <jquelin@mandriva.org> 2.25.0-1mdv2010.1
+ Revision: 528754
- update to 2.025

* Sun Jan 10 2010 Jérôme Quelin <jquelin@mandriva.org> 2.24.0-1mdv2010.1
+ Revision: 488599
- update to 2.024

* Tue Nov 10 2009 Jérôme Quelin <jquelin@mandriva.org> 2.23.0-1mdv2010.1
+ Revision: 463920
- update to 2.023

* Mon Aug 31 2009 Jérôme Quelin <jquelin@mandriva.org> 2.21.0-1mdv2010.0
+ Revision: 422796
- update to 2.021

* Fri Jun 05 2009 Olivier Thauvin <nanardon@mandriva.org> 2.020-1mdv2010.0
+ Revision: 383072
- 2.020

* Fri Jun 05 2009 Olivier Thauvin <nanardon@mandriva.org> 2.019-2mdv2010.0
+ Revision: 383070
- rebuild

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.019-1mdv2010.0
+ Revision: 371905
- update to new version 2.019

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.018-1mdv2010.0
+ Revision: 371662
- new version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.017-1mdv2010.0
+ Revision: 370043
- update to new version 2.017

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.015-2mdv2009.1
+ Revision: 351688
- rebuild

* Fri Sep 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.015-1mdv2009.0
+ Revision: 281095
- update to new version 2.015

* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.012-1mdv2009.0
+ Revision: 236261
- update to new version 2.012

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.011-1mdv2009.0
+ Revision: 209320
- update to new version 2.011

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.010-1mdv2009.0
+ Revision: 201845
- update to new version 2.010

* Tue Apr 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.009-1mdv2009.0
+ Revision: 196469
- update to new version 2.009
- update to new version 2.009

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 2.008-2mdv2008.1
+ Revision: 151462
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 11 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.008-1mdv2008.1
+ Revision: 107971
- update to new version 2.008

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.006-1mdv2008.0
+ Revision: 78093
- update to new version 2.006

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.005-1mdv2008.0
+ Revision: 47125
- update to new version 2.005


* Mon Mar 05 2007 Olivier Thauvin <nanardon@mandriva.org> 2.004-1mdv2007.0
+ Revision: 132884
- 2.004

* Sat Jan 06 2007 Olivier Thauvin <nanardon@mandriva.org> 2.003-1mdv2007.1
+ Revision: 104837
- 2.003

* Mon Nov 13 2006 Olivier Thauvin <nanardon@mandriva.org> 2.001-1mdv2007.1
+ Revision: 83935
- first mdv package
- Create perl-Compress-Raw-Bzip2

