Summary:	Crimson - Java API for XML Processing (JAXP)
Summary(pl):	Crimson - API Javy do przetwarzania XML-a (JAXP)
Name:		crimson
Version:	1.1.3
Release:	1
License:	Apache/W3C/Public Domain
Group:		Development/Languages/Java
Source0:	http://xml.apache.org/dist/crimson/%{name}-%{version}-src.tar.gz
# Source0-md5:	bb0a5fe59fd28ce5bfc4b22baeca12c1
URL:		http://xml.apache.org/crimson/
BuildRequires:	ant >= 1.3
BuildRequires:	jdk
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
This version of Crimson supports the Java API for XML Processing
(JAXP) version 1.1 specification by providing implementations for the
following package hierarchies: javax.xml.parsers, org.w3c.dom,
org.xml.sax.*. Note that the javax.xml.transform hierarchy is not
supported. One known implementation of the javax.xml.transform
hierarchy is Xalan 2.

%description -l pl
Ta wersja Crimson dostarcza API Javy do przetwarzania XML-a (JAXP)
zgodne ze specyfikacj± wersji 1.1 poprzez dostarczenie implementacji
nastêpuj±cych hierarchii: javax.xml.parsers, org.w3c.dom,
org.xml.sax.*. Uwaga: hierarchia javax.xml.transform nie jest
obs³ugiwana. Jedn± z implementacji tej hierarchii jest Xalan 2.

%package doc
Summary:	Crimson JAXP implementation - documentation
Summary(pl):	Crimson, implementacja JAXP - dokumentacja
Group:		Development/Languages/Java

%description doc
Crimson JAXP implementation - documentation.

%description doc -l pl
Crimson, implementacja JAXP - dokumentacja.

%prep
%setup -q

%build
if [ "-z $JAVA_HOME" ]; then
	JAVA_HOME=%{_libdir}/java
fi

ant jars docs %{!?debug:-Ddebug=off -Doptimize=true}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install build/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.txt
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc build/docs build/examples
