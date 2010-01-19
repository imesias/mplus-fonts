###############################################################################
# Definitions
###############################################################################
%define fixed_desc() \
The combination of fixed-fullwidth M+ %2 for Japanese and fixed-halfwidth \
%1 %2 %3 for alphabets. They are 5 weights from Thin to Bold.   

%define proportional_desc() \
The combination of fixed-fullwidth M+ %2 for Japanese and proportional  \
%1 %2 %3 for alphabets. They are 7 weights from Thin to Black.         

%define common_desc() \
The Mplus fonts are 7 families of fonts, of which 4 are combinations \
of proportional font families,variations of fixed-fullwidth fonts, \
variations of fixed-halfwidth fonts and each have between 5 - 7 \
different weights.

%define summary_p M+ P is aimed as sophisticated and relaxed design

%define summary_c M+ C is optimized to be proportioned and has two variations

%define summary_m M+ M emphasize the balance of natural letterform and high legibility


%define fontname mplus

###############################################################################
# Header
###############################################################################

Name:       %{fontname}-fonts
Version:    028 
Release:    1%{?dist}
Summary:    The Mplus fonts is a superfamily of fonts designed by Coji Morishita

Group:      User Interface/X    
License:    mplus
URL:        http://%{fontname}-fonts.sourceforge.jp/%{fontname}-outline-fonts/index-en.html
Source0:    http://downloads.sourceforge.jp/%{fontname}-fonts/6650/%{fontname}-TESTFLIGHT-%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch: noarch  
BuildRequires:   fontpackages-devel  

%description
%common_desc

###############################################################################
# Package section
###############################################################################

%package common
Summary:  Mplus, common files (documentation…)
Requires: fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


# 1p
%package -n %{fontname}-1p-fonts
Summary: %summary_p
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-1p-fonts
%proportional_desc M+ 1P Type-1

%_font_pkg -n %{fontname}-1p %{fontname}-1p-*.ttf

# 2p
%package -n %{fontname}-2p-fonts
Summary: %summary_p
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-2p-fonts
%proportional_desc M+ 2P Type-2

%_font_pkg -n %{fontname}-2p %{fontname}-2p-*.ttf

# 1c
%package -n %{fontname}-1c-fonts
Summary: %summary_c
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-1c-fonts
%proportional_desc M+ 1C Type-1

%_font_pkg -n %{fontname}-1c %{fontname}-1c-*.ttf

# 2c
%package -n %{fontname}-2c-fonts
Summary: %summary_c
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-2c-fonts
%proportional_desc M+ 2C Type-2

%_font_pkg -n %{fontname}-2c %{fontname}-2c-*.ttf

# 1m
%package -n %{fontname}-1m-fonts
Summary: %summary_m
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-1m-fonts
%fixed_desc M+ 1M Type-1

%_font_pkg -n %{fontname}-1m %{fontname}-1m-*.ttf

# 2m
%package -n %{fontname}-2m-fonts
Summary: %summary_m
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-2m-fonts
%fixed_desc M+ 2M Type-2

%_font_pkg -n %{fontname}-2m %{fontname}-2m-*.ttf

# 1mn
%package -n %{fontname}-1mn-fonts
Summary: %summary_m
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-1mn-fonts
%fixed_desc M+ 1MN Type-1

%_font_pkg -n %{fontname}-1mn %{fontname}-1mn-*.ttf

###############################################################################
# Files
###############################################################################
%prep
%setup -q -n %{fontname}-TESTFLIGHT-%{version}

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

%clean
rm -fr %{buildroot}

%files common
%defattr(0644,root,root,0755)
%doc LICENSE_{E,J} README_{E,J}

%changelog
* Tue Jan 12 2010 Igshaan Mesias <igshaan.mesias@gmail.com> - 028-1
- Initial Release

