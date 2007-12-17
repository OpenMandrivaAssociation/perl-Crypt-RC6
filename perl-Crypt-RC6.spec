%define real_name Crypt-RC6

Summary:	Crypt-RC6 module for perl 
Name:		perl-%{real_name}
Version:	1.0
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel

%description
This is a perl module which implements a Crypt::CBC compliant 
RC6 block cipher encryption module.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYING README
%{perl_vendorlib}/*/Crypt/RC6.pm
%{perl_vendorlib}/*/auto/Crypt/RC6
%{_mandir}/*/*


