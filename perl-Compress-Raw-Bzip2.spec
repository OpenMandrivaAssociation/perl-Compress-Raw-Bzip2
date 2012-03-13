%define	upstream_name		Compress-Raw-Bzip2
%define	upstream_version	2.049

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Low-Level Interface to bzip2 compression library
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	bzip2-devel
BuildRequires:	perl-devel

%description
Low-Level Interface to bzip2 compression library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
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
