from enum import Enum

class Daemon(Enum):
    thermalmonitord = ["com.apple.thermalmonitord"]
    OTA = [
        "com.apple.mobile.softwareupdated",
        "com.apple.OTATaskingAgent",
        "com.apple.softwareupdateservicesd"
    ]
    UsageTrackingAgent = ["com.apple.UsageTrackingAgent"]
    GameCenter = ["com.apple.gamed"]
    ScreenTime = [
        "com.apple.ScreenTimeAgent",
        "com.apple.homed",
        "com.apple.tvremoted",
        "com.apple.TVRemoteConnectionService",
        "com.apple.newsd",
        "com.apple.CarPlayApp",
#        "com.apple.carkitd",
        "com.apple.sidecar-relay",
        "com.apple.handwritingd",
#        "com.apple.dmd",
        "com.apple.handoffd",
        "com.apple.watchlistd",
#        "com.apple.businessservicesd",
        "com.apple.bookdatastored",
        "com.apple.bookassetd",
        "com.apple.videosubscriptionsd",
        "com.apple.VideoSubscriberAccount.DeveloperService",
        "com.apple.VideoSubscriberAccount.PrivacyService",
        "com.apple.familycircled",
        "com.apple.familynotificationd",
        "com.apple.exchangesyncd",
        "com.apple.calaccessd",
        "com.apple.managedconfiguration.mdmd",
        "com.apple.managedconfiguration.passcodenagd",
        "com.apple.remotemanagementd",
        "com.apple.mobilestoredemod",
        "com.apple.mobilestoredemodhelper",
        "com.apple.progressd",
        "com.apple.classkitd",
        "com.apple.studentd"
    ]
    CrashReports = [
        "com.apple.ReportCrash",
        "com.apple.ReportCrash.Jetsam",
        "com.apple.ReportMemoryException",
        "com.apple.OTACrashCopier",
        "com.apple.analyticsd",
        "com.apple.wifianalyticsd",
        "com.apple.aslmanager",
        "com.apple.coresymbolicationd",
        "com.apple.crash_mover",
        "com.apple.crashreportcopymobile",
        "com.apple.DumpBasebandCrash",
        "com.apple.DumpPanic",
        "com.apple.logd",
        "com.apple.logd.admin",
        "com.apple.logd.events",
        "com.apple.logd.watchdog",
        "com.apple.logd_helper",
        "com.apple.logd_reporter",
        "com.apple.logd_reporter.report_statistics",
        "com.apple.system.logger",
        "com.apple.hangreporter",
        "com.apple.hangtracerd",
        "com.apple.spindump",
        "com.apple.rtcreportingd",
        "com.apple.syslogd",
        "com.apple.signpost.signpost_reporter",
        "com.apple.pluginkit.pkreporter",
        "com.apple.ProxiedCrashCopier",
        "com.apple.ProxiedCrashCopier.ProxyingDevice",
        "com.apple.ReportSystemMemory",
        "com.apple.osanalytics.osanalyticshelper",
        "com.apple.osanalyticsd",
        "com.apple.metrickitd",
#        "com.apple.triald",
        "com.apple.siri-distributed-evaluation"
#        "com.apple.suggestd"
    ]
    Diagnostics = [
        "com.apple.diagnosticd",
        "com.apple.diagnosticextensionsd",
        "com.apple.diagnosticservicesd",
        "com.apple.diagnosticspushd",
        "com.apple.symptomsd-diag",
        "com.apple.sysdiagnose",
        "com.apple.sysdiagnose.darwinos",
        "com.apple.sysdiagnose_helper",
        "com.apple.iosdiagnosticsd",
        "com.apple.awdd",
#        "com.apple.adid",
        "com.apple.ap.adservicesd",
        "com.apple.ap.adprivacyd",
        "com.apple.ap.promotedcontentd",
        "com.apple.tailspind",
        "com.apple.asd",
        "com.apple.perfdiagsselfenabled",
        "com.apple.pcapd",
        "com.apple.aspcarrylog",
        "com.apple.CAReportingService",
        "com.apple.checkerboard",
        "com.apple.checkerboardd",
        "com.apple.managedconfiguration.teslad",
        "com.apple.accessibility.axAuditDaemon.deviceservice"
    ]
    ATWAKEUP = [
        "com.apple.atc.atwakeup",
        "com.apple.atrun"
    ]
    Tips = ["com.apple.tipsd"]
    VPN = ["com.apple.racoon"]
    ChineseLAN = [
        "com.apple.wapic",
        "com.apple.wifi.wapic",
        "com.apple.bootpd",
        "com.apple.ftp-proxy-embedded"
    ]
    HealthKit = [
#        "com.apple.healthd",
        "com.apple.matd",
        "com.apple.fitcore",
        "com.apple.fitcore.session"
    ]
    AirPrint = ["com.apple.printd"]
    AssistiveTouch = [
        "com.apple.assistivetouchd",
        "com.apple.accessibility.guidedaccessd",
        "com.apple.accessibility.colorfilterd",
        "com.apple.accessibility.axvisualalerts",
        "com.apple.accessibility.magnifierd",
        "com.apple.accessibility.remotecontrol",
        "com.apple.accessibility.heard"
    ]
    iCloud = ["com.apple.itunescloudd"]
    InternetTethering = ["com.apple.MobileInternetSharing"]
    PassBook = ["com.apple.passd"]
    Spotlight = [
#        "com.apple.searchd",
        "com.apple.corespotlightservice",
        "com.apple.corespotlightd",
        "com.apple.spotlightknowledged",
        "com.apple.spotlightknowledged.updater"
#        "com.apple.spotlight.IndexAgent",
#        "com.apple.relevanced",
#        "com.apple.relevanced.ios"
    ]
    VoiceControl = [
#        "com.apple.assistant_service",
#        "com.apple.assistantd",
        "com.apple.voiced",
        "com.apple.accessibility.speechd",
        "com.apple.voiceserverd",
#        "com.apple.siriinferenced",
#        "com.apple.speechsynthesisd",
        "com.apple.commandandcontrol",
        "com.apple.VoiceOverTouch",
        "com.apple.accessibility.voiceovertrainingd"
    ]
    NanoTimeKit = [
        "com.apple.nanotimekitcompaniond",
#        "com.apple.nanoregistryd",
#        "com.apple.nanoregistrylaunchd",
        "com.apple.nanobackupd",
        "com.apple.nanoprefsyncd",
        "com.apple.nanosystemsettingsd",
        "com.apple.NPKCompanionAgent",
        "com.apple.nptocompaniond",
        "com.apple.resourcegrabberd.companion",
        "com.apple.nanomapscd",
        "com.apple.nanoweatherprefsd",
        "com.apple.nanonewscd",
        "com.apple.nanoappregistryd",
        "com.apple.nanomediaremotelinkagent",
        "com.apple.nanophone.server",
        "com.apple.companioncamerad",
        "com.apple.companionmessagesd",
        "com.apple.companion_proxy",
        "com.apple.companionappd",
        "com.apple.brook.brookcompaniond",
        "com.apple.companionfindlocallyd",
        "com.apple.magicswitchd.companion",
        "com.apple.pairedunlockd-phone",
        "com.apple.pairedsyncd",
        "com.apple.appconduitd",
        "com.apple.ClipServices.clipserviced",
        "com.apple.appclipd",
        "com.apple.appclipsd",
        "com.apple.appclips.events",
        "com.apple.appclips.update",
        "com.apple.appclips.servicesd",
        "com.apple.appclips.appdiscoveryd",
        "com.apple.appstored.AppClipService"
    ]
