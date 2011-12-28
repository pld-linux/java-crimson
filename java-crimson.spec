# From homepage: 2010/08/06 - Apache Crimson has been retired.
Summary:	Crimson - Java API for XML Processing (JAXP)
Summary(pl.UTF-8):	Crimson - API Javy do przetwarzania XML-a (JAXP)
Name:		java-crimson
Version:	1.1.3
Release:	2
License:	Apache/W3C/Public Domain
Group:		Development/Languages/Java
Source0:	http://xml.apache.org/dist/crimson/%{name}-%{version}-src.tar.gz
# Source0-md5:	bb0a5fe59fd28ce5bfc4b22baeca12c1
URL:		http://xml.apache.org/crimson/
BuildRequires:	ant >= 1.3
BuildRequires:	java-commons-net
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java-commons-net
Requires:	jpackage-utils
Provides:	java(jaxp_transform_impl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This version of Crimson supports the Java API for XML Processing
(JAXP) version 1.1 specification by providing implementations for the
following package hierarchies: javax.xml.parsers, org.w3c.dom,
org.xml.sax.*. Note that the javax.xml.transform hierarchy is not
supported. One known implementation of the javax.xml.transform
hierarchy is Xalan 2.

%description -l pl.UTF-8
Ta wersja Crimson dostarcza API Javy do przetwarzania XML-a (JAXP)
zgodne ze specyfikacją wersji 1.1 poprzez dostarczenie implementacji
następujących hierarchii: javax.xml.parsers, org.w3c.dom,
org.xml.sax.*. Uwaga: hierarchia javax.xml.transform nie jest
obsługiwana. Jedną z implementacji tej hierarchii jest Xalan 2.

%package doc
Summary:	Crimson JAXP implementation - documentation
Summary(pl.UTF-8):	Crimson, implementacja JAXP - dokumentacja
Group:		Documentation

%description doc
Crimson JAXP implementation - documentation.

%description doc -l pl.UTF-8
Crimson, implementacja JAXP - dokumentacja.

%prep
%setup -q

%build
CLASSPATH=$(build-classpath commons-net)
%ant jars docs %{!?debug:-Ddebug=off -Doptimize=true}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a build/*.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.txt
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc build/docs build/examples
