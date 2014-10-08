%define	modname	Compress-Raw-Bzip2
%define upstream_version 2.064

Summary:	Low-Level Interface to bzip2 compression library
Name:		perl-%{modname}
Version:	%perl_convert_version %{upstream_version}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/Compress-Raw-Bzip2-%{upstream_version}.tar.gz
BuildRequires:	bzip2-devel
BuildRequires:	perl-devel

%description
Low-Level Interface to bzip2 compression library.

%prep
%setup -qn %{modname}-%{upstream_version}

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


