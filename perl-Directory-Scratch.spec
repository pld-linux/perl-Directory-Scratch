#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Directory
%define	pnam	Scratch
# Source0-md5:	3383a99139c3c8d6fe8bb5fcffb2dd84
Summary:	Directory::Scratch - Easy-to-use self-cleaning scratch space
#Summary(pl):
Name:		perl-Directory-Scratch
Version:	0.13
Release:	1
License:	Perl
Group:		Development/Languages/Perl
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Source0:	http://www.cpan.org/modules/by-modules/Directory/Directory-Scratch-%{version}.tar.gz
%if %{with tests}
BuildRequires:	perl(File::Slurp) >= 9999.12
# version is just because it failed on 0.12 here, even if makefile dont specify minimum version
BuildRequires:	perl(Path::Class) > 0.12
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description


# %description -l pl # TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mv t/os/win32.t{,.off}
mv t/os/mac.t{,.off}

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
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Directory/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
