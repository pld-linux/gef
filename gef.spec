# TODO:
# javadoc package
Summary:	A diagram editing framework
Name:		gef
Version:	0.10.7
Release:	0.1
License:	Apache License
Source0:	http://gef.tigris.org/files/documents/9/10445/GEF-%{version}-src.zip
# Source0-md5:	bb4c1f5e902bbe9ad882794e88994e4c
Url:		http://gef.tigris.org/
Requires:	jakarta-log4j
BuildRequires:	jakarta-ant
BuildRequires:	jakarta-commons-logging
Group:		Development/Languages/Java
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of the GEF project is to build a graph editing library that
can be used to construct many, high-quality graph editing appications.
Some of GEF's features are:
- A simple, concrete design that makes the framework easy to
  understand and extend.
- Node-Port-Edge graph model that is powerful enough for the vast
  majority of connectied graph applications.
- Model-View-Controller design based on the Swing Java UI library
  makes GEF able to act as a UI to existing data structures, and also
  minimizing learning time for developers familiar with Swing.
- High-quality user interactions for moving, resizeing, reshaping,
  etc. GEF also supports several novel interactions such as the broom
  alignment tool and section-action-buttons.
- Generic properties sheet based on JavaBeans introspection.
- XML-based file formats based on the PGML standard (soon to support
  SVG).

%package	doc
Summary:	Javadoc for %{name}
Group:		Documentation

%description	doc
Javadoc for %{name}.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -c -T
mkdir src
cd src
unzip -q %{SOURCE0}
# remove binary files
find . -name "*.jar" -exec rm -f {} \;

%build
cd src
ant package

%install
rm -rf $RPM_BUILD_ROOT
install -D lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/COPYRIGHT src/INSTALL.txt src/readme.txt
%{_javadir}/*
