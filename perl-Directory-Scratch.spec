#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Directory
%define	pnam	Scratch
Summary:	Directory::Scratch - Easy-to-use self-cleaning scratch space
Summary(pl.UTF-8):	Directory::Scratch - łatwa w użyciu samoczyszcząca przestrzeń robocza
Name:		perl-Directory-Scratch
Version:	0.18
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Directory/Directory-Scratch-%{version}.tar.gz
# Source0-md5:	66ea2b47c1bb184b08ba562d14727fb4
URL:		http://search.cpan.org/dist/Directory-Scratch/
BuildRequires:	perl-Module-Build-Tiny
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-Slurp >= 9999.12
# version is just because it failed on 0.12 here, even if makefile doesn't specify minimum version
BuildRequires:	perl-Path-Class > 0.12
BuildRequires:	perl-Path-Tiny >= 0.060
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Directory::Scratch - Easy-to-use self-cleaning scratch space.

%description -l pl.UTF-8
Directory::Scratch - łatwa w użyciu samoczyszcząca przestrzeń robocza.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__mv} t/os/win32.t{,.off}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Directory
%{perl_vendorlib}/Directory/Scratch.pm
%{_mandir}/man3/Directory::Scratch.3pm*
%{_examplesdir}/%{name}-%{version}
