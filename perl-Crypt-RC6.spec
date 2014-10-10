%define real_name Crypt-RC6

Summary:	Crypt-RC6 module for perl 
Name:		perl-%{real_name}
Version:	1.0
Release:	10
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0-9
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.0-8
+ Revision: 680867
- mass rebuild

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.0-7mdv2011.0
+ Revision: 555459
- rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-6mdv2010.0
+ Revision: 430384
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2009.0
+ Revision: 256340
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2008.1
+ Revision: 152040
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-2mdv2008.1
+ Revision: 136950
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdk
- initial Mandriva package

